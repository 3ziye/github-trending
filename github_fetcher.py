#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 热门项目获取器
支持获取 GitHub 热门项目信息并生成详细的 Markdown 报告
"""

import requests
import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import argparse
import sys

class GitHubFetcher:
    def __init__(self, token: str = None):
        """
        初始化 GitHub API 客户端
        
        Args:
            token: GitHub Personal Access Token (可选)
        """
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Trending-Reporter/1.0"
        }
        
        if token:
            self.headers["Authorization"] = f"token {token}"
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_trending_repos(self, language: str = "", time_range: str = "daily", per_page: int = 30) -> List[Dict]:
        """
        获取热门仓库列表
        
        Args:
            language: 编程语言过滤 (如: python, javascript)
            time_range: 时间范围 (daily, weekly, monthly)
            per_page: 每页返回数量
            
        Returns:
            热门仓库列表
        """
        # 计算日期范围
        date_map = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30
        }
        
        days_ago = date_map.get(time_range, 1)
        since_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        # 构建搜索查询
        query_parts = [f"created:>={since_date}"]
        if language:
            query_parts.append(f"language:{language}")
        
        query = " ".join(query_parts)
        
        url = f"{self.base_url}/search/repositories"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": per_page
        }
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get("items", [])
            
        except requests.exceptions.RequestException as e:
            print(f"获取热门仓库失败: {e}")
            return []
    
    def get_repo_details(self, owner: str, repo: str) -> Dict:
        """
        获取仓库详细信息
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            
        Returns:
            仓库详细信息
        """
        url = f"{self.base_url}/repos/{owner}/{repo}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"获取仓库 {owner}/{repo} 详情失败: {e}")
            return {}
    
    def get_repo_readme(self, owner: str, repo: str) -> str:
        """
        获取仓库 README 内容
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            
        Returns:
            README 内容
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/readme"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            
            readme_data = response.json()
            if readme_data.get("encoding") == "base64":
                import base64
                content = base64.b64decode(readme_data["content"]).decode("utf-8", errors="ignore")
                return content
            
        except requests.exceptions.RequestException as e:
            print(f"获取仓库 {owner}/{repo} README 失败: {e}")
        
        return ""
    
    def get_repo_languages(self, owner: str, repo: str) -> Dict:
        """
        获取仓库使用的编程语言
        
        Args:
            owner: 仓库所有者
            repo: 仓库名称
            
        Returns:
            语言使用情况
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"获取仓库 {owner}/{repo} 语言信息失败: {e}")
            return {}
    
    def save_data(self, data: List[Dict], filename: str = "github_trending.json"):
        """
        保存数据到 JSON 文件
        
        Args:
            data: 要保存的数据
            filename: 文件名
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"数据已保存到 {filename}")
            
        except Exception as e:
            print(f"保存数据失败: {e}")
    
    def load_data(self, filename: str = "github_trending.json") -> List[Dict]:
        """
        从 JSON 文件加载数据
        
        Args:
            filename: 文件名
            
        Returns:
            加载的数据
        """
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception as e:
            print(f"加载数据失败: {e}")
        
        return []
    
    def fetch_and_enrich_repos(self, language: str = "", time_range: str = "daily", 
                              per_page: int = 10, save_to_file: bool = True) -> List[Dict]:
        """
        获取并丰富仓库数据
        
        Args:
            language: 编程语言过滤
            time_range: 时间范围
            per_page: 每页数量
            save_to_file: 是否保存到文件
            
        Returns:
            丰富后的仓库数据
        """
        print("正在获取热门仓库...")
        repos = self.get_trending_repos(language, time_range, per_page)
        
        enriched_repos = []
        
        for i, repo in enumerate(repos, 1):
            print(f"处理仓库 {i}/{len(repos)}: {repo['full_name']}")
            
            # 获取详细信息
            owner = repo["owner"]["login"]
            name = repo["name"]
            
            # 获取 README
            readme_content = self.get_repo_readme(owner, name)
            
            # 获取语言信息
            languages = self.get_repo_languages(owner, name)
            
            # 构建丰富的数据结构
            enriched_repo = {
                "basic_info": {
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "owner": repo["owner"]["login"],
                    "description": repo.get("description", ""),
                    "url": repo["html_url"],
                    "clone_url": repo["clone_url"],
                    "ssh_url": repo["ssh_url"],
                    "homepage": repo.get("homepage"),
                    "created_at": repo["created_at"],
                    "updated_at": repo["updated_at"],
                    "pushed_at": repo["pushed_at"]
                },
                "stats": {
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    "watchers": repo["watchers_count"],
                    "open_issues": repo.get("open_issues_count", 0),
                    "size": repo["size"]
                },
                "tech_info": {
                    "language": repo.get("language"),
                    "languages": languages,
                    "license": repo.get("license", {}).get("name") if repo.get("license") else None,
                    "topics": repo.get("topics", [])
                },
                "content": {
                    "readme": readme_content[:5000] if readme_content else "",  # 限制长度
                    "default_branch": repo.get("default_branch", "main")
                },
                "fetched_at": datetime.now().isoformat()
            }
            
            enriched_repos.append(enriched_repo)
            
            # 避免API限流
            time.sleep(1)
        
        # if save_to_file:
        #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #     filename = f"github_trending_{timestamp}.json"
        #     self.save_data(enriched_repos, filename)
        
        return enriched_repos


def main():
    parser = argparse.ArgumentParser(description="GitHub 热门项目获取器")
    parser.add_argument("--language", "-l", default="", help="编程语言过滤")
    parser.add_argument("--time-range", "-t", choices=["daily", "weekly", "monthly"], 
                       default="daily", help="时间范围")
    parser.add_argument("--count", "-c", type=int, default=10, help="获取数量")
    parser.add_argument("--token", help="GitHub Personal Access Token")
    parser.add_argument("--output", "-o", default="", help="输出文件名")
    
    args = parser.parse_args()
    
    # 创建获取器实例
    fetcher = GitHubFetcher(token=args.token)
    
    # 获取数据
    repos = fetcher.fetch_and_enrich_repos(
        language=args.language,
        time_range=args.time_range,
        per_page=args.count,
        save_to_file=bool(args.output)
    )
    
    if args.output:
        fetcher.save_data(repos, args.output)
    
    print(f"成功获取 {len(repos)} 个热门仓库的详细信息")


if __name__ == "__main__":
    main()
