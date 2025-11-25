[![Go Report Card](https://goreportcard.com/badge/github.com/rshdhere/vibecheck)](https://goreportcard.com/report/github.com/rshdhere/vibecheck)
[![codecov](https://codecov.io/gh/rshdhere/vibecheck/branch/main/graph/badge.svg)](https://codecov.io/gh/rshdhere/vibecheck)


<img width="506" height="114" alt="ascii-art-text" src="https://github.com/user-attachments/assets/2391e58e-5646-4c1a-a624-23ebb0dde208" />



A Cross-Platform Command-Line AI-tool for automating git commit messages by outsourcing them to LLMs. Supports multiple providers including OpenAI, Gemini, Anthropic, Groq, Grok, Kimi K2, Qwen, DeepSeek, Perplexity Sonar, and Ollama.

## Installation
### macOS/linux
```bash
curl -fsSL https://install.raashed.xyz | bash
```
### windows

```powershell
iwr https://install.raashed.xyz/install.ps1 -useb | iex
```

> **Important :** Make sure to run the command as an `administrator` using Powershell.
### macOS (brew)
```bash
brew install vibecheck
```
>  <img width="725" height="500" alt="image" src="https://github.com/user-attachments/assets/175572fa-c283-435b-b3c1-9dac2e5232cd" />



## The Ultimate One Liner

```bash
vibecheck commit
```
> **Note :** Make sure you stage your files, right before you check that it passes the vibecheck ;)

## Demonstration

![full-demo-vibecheck](https://github.com/user-attachments/assets/e8cd1f16-34bb-4356-a07b-03271c0d926c)

## More Features
```bash
vibecheck dashboard
```
> **Dashboard :** It keeps the tab of the commits you generated and money you saved with vibecheck
>
![dashboard-cut](https://github.com/user-attachments/assets/e45d09f6-bc3a-41cf-a8aa-d26e21a04880)

```bash
vibecheck keys
```

> **Keys :** It keeps your keys globally accessable to vibecheck, so that you always dont have to introduce a environmental variable
>
![vibecheck-keys](https://github.com/user-attachments/assets/815f6ef9-55db-4eca-99d9-7e09957f0a81)

```bash
vibecheck models
```
> **Models :** You can switch the models for better latency and accuracy all along
>
![models](https://github.com/user-attachments/assets/d9aa6645-5876-427f-8633-310be70dbfe8)

```mermaid

flowchart TD

    %% Nodes Styling

    classDef user fill:#f9f,stroke:#333,stroke-width:2px,color:black;

    classDef system fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:black;

    classDef external fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:black;

    classDef error fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:black;



    Start([User Action]) --> InstallCheck{Is vibecheck installed?}

    class Start user



    %% Installation Branch

    InstallCheck -- No --> OS{Select OS}

    OS -- macOS/Linux --> Curl[Run curl command]

    OS -- Windows --> PS[Run PowerShell as Admin]

    OS -- macOS Brew --> Brew[Run brew install]

    Curl & PS & Brew --> Config[Setup API Keys]

    Config --> EnvVars[Export vars OR .env file]

    Config --> KeysCmd[vibecheck keys]

    KeysCmd --> KeysFile[Store in ~/.vibecheck_keys.json]



    %% Main Execution

    InstallCheck -- Yes --> Command{Run Command}

    EnvVars -.-> Command

    KeysFile -.-> Command



    %% Branch: UPGRADE

    Command -- "vibecheck upgrade" --> PermCheck{Protected Dir?}

    PermCheck -- Yes --> Sudo[Auto-run with Sudo] --> UpdateBin[Download & Replace Binary]

    PermCheck -- No --> UpdateBin

    UpdateBin --> End([Done])



    %% Branch: DASHBOARD/MODELS/KEYS

    Command -- "vibecheck dashboard" --> ShowDash[Read Logs] --> DisplayStats[Show Commits & $$ Saved] --> End

    Command -- "vibecheck models" --> ShowMods[List Supported Models] --> SwitchMod[Switch Model Preference] --> End

    Command -- "vibecheck keys" --> KeysUI[Interactive Keys Manager] --> KeysList[List Providers with Status] --> KeysEdit[Add/Edit/Delete Keys] --> KeysSave[Save to ~/.vibecheck_keys.json] --> End



    %% Branch: COMMIT (Core Feature)

    Command -- "vibecheck commit" --> GitCheck{Files Staged?}

    

    %% Git Check Logic

    GitCheck -- No --> ErrStage[Error: Stage files first!]:::error

    ErrStage --> End

    

    GitCheck -- Yes --> KeyCheck{API Key Found?}

    %% Key Lookup Priority
    KeyCheck --> CheckEnv{Check .env file}
    CheckEnv -- Found --> KeyFound[Use Key]
    CheckEnv -- Not Found --> CheckExport{Check export vars}
    CheckExport -- Found --> KeyFound
    CheckExport -- Not Found --> CheckKeysFile{Check vibecheck keys}
    CheckKeysFile -- Found --> KeyFound
    CheckKeysFile -- Not Found --> ErrKey[Error: Missing API Key]:::error

    ErrKey --> Config

    KeyFound --> ProviderSelect{Provider Flag?}

    

    %% Provider Logic

    ProviderSelect -- Default --> DefModel[Default Model]

    ProviderSelect -- "--provider X" --> SelectModel[Select Specific Provider]

    

    subgraph AI_Providers [External AI Cloud / Local]

        direction LR

        OpenAI

        Gemini

        Anthropic

        Groq

        XAI_Grok

        Kimi

        Qwen

        DeepSeek

        Perplexity

        Ollama_Local

    end

   