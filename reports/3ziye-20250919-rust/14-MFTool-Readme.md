# Description

MFTool is a red team-oriented NTFS parser. Instead of asking Windows for files, it parses the on-disk structures of a mounted NTFS volume directly to build an in-memory copy of the [Master File Table](https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table). That in-memory MFT is kept encrypted and is then used to:

- Search the entire disk for files and metadata.
- Retrieve file contents **without opening an OS-level file handle**, enabling access to data that is typically locked by the operating system (e.g., `SAM`, `NTUSER.dat`, `SYSTEM`, `pagefile.sys`, etc.) as well as deleted files (hereafter referred to as "hidden").

Direct NTFS parsing is not new and is widely used in forensics, although this tool has been developed taking into account the needs and requirements from a red team perspective. Also, I wasn't able to find a public tool that performs in the way I pictured it, so I decided to create my own NTFS parser.

# Content

- [How it works](#How-it-works)
- [How to use it](#How-to-use-it)
- [Commands](#Commands)
- [Examples](#Examples)
  - [Retrieving metadata of an entry](#Retrieving-metadata-of-an-entry)
  - [Accessing deleted and locked files](#Accessing-deleted-and-locked-files)
  - [Directory listing and regex-based search](#Directory-listing-and-regex-based-search)
- [Limitations and Known Issues](#Limitations-and-Known-Issues)
- [Links](#Links)

# How it works

MFTool interacts directly with a mounted NTFS volume by opening a handle to it and parsing the on-disk filesystem structures. Instead of relying on Windows APIs, it walks through the Master File Table to build an internal representation of the filesystem.

1. **Boot sector parsing**  
   Once a handle to the volume is opened, MFTool parses the boot sector to locate the offset of the first MFT entry. From there, it follows the cluster chains to enumerate the rest of the entries.

2. **MFT entry reconstruction**  
   Each MFT record is reconstructed by replacing the Update Sequence Number (USN) with the corresponding values from the Update Sequence Array (USA). The reconstructed entries are stored in an encrypted in-memory cache to prevent accidental data leakage. This cache is rebuilt every time a new target volume is selected.

3. **File content retrieval**  
   To read a file, MFTool does not rely on an OS-level file handle. Instead, it parses the file's MFT entry, extracts the unnamed `$DATA` attribute, and follows its data run list to locate the clusters containing the file's content.  
   - Data is read directly from disk offsets, ignoring Windows' file access controls (note that administrative privileges are still required to run the tool, so this should not be considered an ACL bypass per se).  
   - If the file is compressed, the content is split into logical units and decompressed using [`RtlDecompressBuffer`](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-rtldecompressbuffer).  
   - This allows retrieval of normal, locked, and even deleted files in case the content is still present in the disk.   

4. **Searching and directory listing**  
   File search and directory enumeration rely on parsing the `$I30` index attributes (`INDEX_ROOT`, `INDEX_ALLOCATION` structures). This allows for efficient lookups with logarithmic complexity `O(log n)`, and supports both exact name matching and regex-based searches (regex-based searches are not logarithmic tho).

5. **Reparse point handling**  
   The parser currently resolves reparse points of type **symlink** and **mount point**, ensuring correct navigation across linked or mounted paths.  

# How to use it

To build the tool just compile it in `release` mode:

	C:\Path\To\MFTool> cargo build --release

Once executed, the tool will wait for commands out of the list commented in the next section.

# Commands

## set_target
Sets the target volume to be parsed.  
This command expects a string pointing to a mounted NTFS volume, either by drive letter or by volume GUID path (e.g., `\\.\C:` or `\\?\Volume{04171d6a-0000-0000-0000-100000000000}`).  
Once a valid volume path is provided, MFTool rebuilds its in-memory cache of the MFT. From this point, all further interactions with the volume are performed against that cache.

## rebuild
Rebuilds the in-memory MFT cache for the current target volume.  

## ls
Parses the `$I30` index attributes to list the files contained in a directory.  
Both the Win32 name and the DOS (short) name (if any) of each file are displayed.

## show
Given a directory path and a filename, retrieves the metadata stored in the file's MFT entry.

## show_by_id
Same as `show`, but instead of requiring a path and filename, it expects the MFT entry index.

## show_by_regex
Searches for files across the entire volume using a regular expression (expressed as `/regex/`).  
This command performs a sequential search of all MFT entries, so its complexity is linear.  
If invoked with the `hidden` flag, it restricts th