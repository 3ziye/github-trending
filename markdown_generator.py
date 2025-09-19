#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 项目 Markdown 报告生成器
基于项目数据生成详细的 Markdown 格式报告
"""

import json
import re
import os
from datetime import datetime
from typing import Dict, List, Any
import argparse

class MarkdownReportGenerator:
    def __init__(self):
        self.template_sections = {
            "header": self._generate_header,
            "summary": self._generate_summary,
            "projects": self._generate_projects_section,
            "footer": self._generate_footer
        }
    
    def generate_report(self, data: List[Dict], output_file: str = "", title: str = "GitHub 热门项目报告"):
        """
        生成完整的 Markdown 报告
        
        Args:
            data: 项目数据列表
            output_file: 输出文件名
            title: 报告标题
        """
        if not data:
            print("没有数据可生成报告")
            return
        
        # 生成报告内容
        report_content = []
        
        # 头部
        report_content.append(self._generate_header(title, len(data)))
        
        # 摘要
        report_content.append(self._generate_summary(data))
        
        # 项目详情
        report_content.append(self._generate_projects_section(data))
        
        # 脚注
        report_content.append(self._generate_footer())
        
        # 合并内容
        full_report = "\n\n".join(report_content)
        
        # 输出到文件或控制台
        if output_file:
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(full_report)
                print(f"报告已生成: {output_file}")
            except Exception as e:
                print(f"写入文件失败: {e}")
        else:
            print(full_report)
    
    def _generate_header(self, title: str, project_count: int) -> str:
        """生成报告头部"""
        current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M")
        
        header = f"""# {title}

<div align="center">
📊 <strong>生成时间</strong>: {current_time}  •  
🎯 <strong>项目数量</strong>: {project_count} 个  •  
🔥 <strong>数据来源</strong>: GitHub API
</div>

---"""
        
        return header
    
    def _generate_summary(self, data: List[Dict]) -> str:
        """生成报告摘要"""
        # 统计信息
        languages = {} 
        total_stars = 0
        total_forks = 0
        licenses = {} 
        total_watchers = 0
        total_issues = 0
        topics = {}
        
        for project in data:
            # 统计语言
            lang = project.get("tech_info", {}).get("language")
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
            
            # 统计星标和 fork
            stats = project.get("stats", {})
            total_stars += stats.get("stars", 0)
            total_forks += stats.get("forks", 0)
            total_watchers += stats.get("watchers", 0)
            total_issues += stats.get("open_issues", 0)
            
            # 统计主题标签
            project_topics = tech.get("topics", [])
            for topic in project_topics:
                topics[topic] = topics.get(topic, 0) + 1
            
            # 统计许可证
            license_name = project.get("tech_info", {}).get("license")
            if license_name:
                licenses[license_name] = licenses.get(license_name, 0) + 1
        
        # 排序语言
        top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
        top_licenses = sorted(licenses.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # 排序主题标签
        top_topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)[:10]
        
        summary = f"""## 📈 数据概览

### 🌟 项目统计
- **总星标数**: {total_stars:,}
- **总 Fork 数**: {total_forks:,}
- **总关注数**: {total_watchers:,}
- **开放问题数**: {total_issues:,}
- **平均星标数**: {total_stars // len(data):,}

### 💻 热门编程语言
{self._format_language_stats(top_languages)}

### 📄 许可证分布
{self._format_license_stats(top_licenses)}

### 🏷️ 热门主题标签
{self._format_topic_stats(top_topics)}

---"""
        
        return summary
    
    def _format_language_stats(self, languages: List[tuple]) -> str:
        """格式化语言统计"""
        if not languages:
            return "- 暂无数据"
        
        result = []
        for lang, count in languages:
            result.append(f"- **{lang}**: {count} 个项目")
        
        return "\n".join(result)
    
    def _format_license_stats(self, licenses: List[tuple]) -> str:
        """格式化许可证统计"""
        if not licenses:
            return "- 暂无数据"
        
        result = []
        for license_name, count in licenses:
            result.append(f"- **{license_name}**: {count} 个项目")
        
        return "\n".join(result)
    
    def _format_topic_stats(self, topics: List[tuple]) -> str:
        """格式化主题标签统计"""
        if not topics:
            return "- 暂无数据"
        
        result = []
        for topic, count in topics:
            result.append(f"- `{topic}`: {count} 个项目")
        
        return "\n".join(result)
    
    def _generate_projects_section(self, data: List[Dict]) -> str:
        """生成项目详情部分"""
        projects_md = ["## 🚀 热门项目详情"]
        
        for i, project in enumerate(data, 1):
            project_md = self._generate_single_project(project, i)
            projects_md.append(project_md)
        
        return "\n\n".join(projects_md)
    
    def _generate_single_project(self, project: Dict, index: int) -> str:
        """生成单个项目的 Markdown"""
        basic = project.get("basic_info", {})
        stats = project.get("stats", {})
        tech = project.get("tech_info", {})
        content = project.get("content", {})
        
        # 项目标题
        title = f"### {index}. {basic.get('name', 'Unknown')}"
        
        # 计算项目热度指数 (基于星标数和fork数)
        stars = stats.get('stars', 0)
        forks = stats.get('forks', 0)
        hot_score = int(stars + forks * 0.5) if stars + forks > 0 else 0
        
        # 基本信息 - 使用列表格式
        info_list = [
            f"**项目名称**: [{basic.get('full_name', '')}]({basic.get('url', '')})",
            f"**项目描述**: {(basic.get('description') or '暂无描述')[:120]}{'...' if len(basic.get('description') or '') > 120 else ''}",
            f"**主要语言**: {tech.get('language', '未知')}",
            f"**许可证**: {tech.get('license', '未指定')}",
            f"**⭐ 星标数**: {stars:,}",
            f"**🍴 Fork 数**: {forks:,}",
            f"**👀 关注数**: {stats.get('watchers', 0):,}",
            f"**🐛 开放问题**: {stats.get('open_issues', 0)}",
            f"**最后更新**: {self._format_date(basic.get('updated_at', ''))}"
        ]
        info_text = "\n".join(info_list)
        
        # 核心特性 (从 README 中提取)
        features = self._extract_features(content.get("readme", ""))
        
        # 适用场景 (基于语言和主题推断)
        use_cases = self._generate_use_cases(project)
        
        # 技术栈
        tech_stack = self._generate_tech_stack(tech)
        
        # 项目标签
        project_topics = tech.get("topics", [])
        topics_display = "\n".join([f"- `{topic}`" for topic in project_topics[:8]]) if project_topics else "- 暂无标签"
        
        # 组装项目部分
        project_sections = [
            title,
            f"**🔥 热度指数**: {hot_score:,}",
            info_text,
            f"**🏠 项目主页**: {basic.get('homepage', '无') if basic.get('homepage') else '无'}",
            f"**📂 克隆地址**: `{basic.get('clone_url', '')}`"
        ]
        
        if tech_stack:
            project_sections.append(f"**💻 技术栈**: {tech_stack}")
        
        if project_topics:
            project_sections.append(f"#### 🏷️ 项目标签\n{topics_display}")
        
        if features:
            project_sections.append(f"#### 🎯 核心特性\n{features}")
        
        if use_cases:
            project_sections.append(f"#### 🎨 适用场景\n{use_cases}")
        
        # 添加分隔线，提高可读性
        project_sections.append("---")
        
        return "\n\n".join(project_sections)
    
    def _extract_features(self, readme_content: str) -> str:
        """从 README 中提取核心特性"""
        if not readme_content:
            return ""
        
        # 查找特性相关的章节
        feature_patterns = [
            r"## Features?\s*\n(.*?)(?=\n##|\n#|$)",
            r"## 特性\s*\n(.*?)(?=\n##|\n#|$)",
            r"### Features?\s*\n(.*?)(?=\n###|\n##|\n#|$)",
            r"## What.*\s*\n(.*?)(?=\n##|\n#|$)",
        ]
        
        features_text = ""
        for pattern in feature_patterns:
            match = re.search(pattern, readme_content, re.IGNORECASE | re.DOTALL)
            if match:
                features_text = match.group(1).strip()
                break
        
        if features_text:
            # 清理文本，保留主要内容
            lines = features_text.split('\n')[:5]  # 只取前5行
            cleaned_lines = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('![') and len(line) < 200:
                    if not line.startswith('-') and not line.startswith('*'):
                        line = f"- {line}"
                    cleaned_lines.append(line)
            
            return "\n".join(cleaned_lines) if cleaned_lines else ""
        
        return ""
    
    def _generate_use_cases(self, project: Dict) -> str:
        """根据项目信息生成适用场景"""
        tech = project.get("tech_info", {})
        basic = project.get("basic_info", {})
        
        language = (tech.get("language") or "").lower()
        topics = tech.get("topics", [])
        description = (basic.get("description") or "").lower()
        
        use_cases = []
        
        # 基于编程语言推断
        language_cases = {
            "python": ["数据科学与分析", "机器学习项目", "Web 应用开发", "自动化脚本"],
            "javascript": ["前端Web开发", "Node.js后端服务", "移动应用开发", "桌面应用"],
            "typescript": ["大型前端应用", "类型安全的后端服务", "企业级项目开发"],
            "go": ["微服务架构", "云原生应用", "系统级编程", "高性能后端服务"],
            "rust": ["系统编程", "高性能应用", "区块链开发", "WebAssembly"],
            "java": ["企业级应用", "Spring Boot项目", "Android应用开发", "分布式系统"],
            "c++": ["系统编程", "游戏开发", "高性能计算", "嵌入式开发"],
            "swift": ["iOS应用开发", "macOS应用", "服务端Swift开发"],
            "kotlin": ["Android应用开发", "多平台开发", "服务端开发"],
            "php": ["Web应用开发", "内容管理系统", "电商平台", "API服务"]
        }
        
        if language in language_cases:
            use_cases.extend(language_cases[language][:3])
        
        # 基于主题和描述推断
        topic_cases = {
            "machine-learning": "机器学习模型训练",
            "deep-learning": "深度学习研究",
            "web": "Web应用开发",
            "api": "API服务构建",
            "cli": "命令行工具开发",
            "framework": "应用框架搭建",
            "library": "第三方库集成",
            "docker": "容器化部署",
            "kubernetes": "云原生部署"
        }
        
        for topic in topics:
            if topic.lower() in topic_cases:
                case = topic_cases[topic.lower()]
                if case not in use_cases:
                    use_cases.append(case)
        
        # 基于描述关键词推断
        if "api" in description:
            use_cases.append("API服务开发")
        if "dashboard" in description or "admin" in description:
            use_cases.append("管理后台开发")
        if "blog" in description:
            use_cases.append("博客系统搭建")
        
        # 去重并限制数量
        unique_cases = list(dict.fromkeys(use_cases))[:4]
        
        if unique_cases:
            return "\n".join([f"- {case}" for case in unique_cases])
        
        return "- 通用软件开发\n- 学习参考项目"
    
    def _extract_setup_instructions(self, readme_content: str) -> str:
        """从 README 中提取安装和部署说明"""
        if not readme_content:
            return ""
        
        # 查找安装相关的章节
        setup_patterns = [
            r"## Installation\s*\n(.*?)(?=\n##|\n#|$)",
            r"## 安装\s*\n(.*?)(?=\n##|\n#|$)",
            r"## Getting Started\s*\n(.*?)(?=\n##|\n#|$)",
            r"## Quick Start\s*\n(.*?)(?=\n##|\n#|$)",
            r"## Setup\s*\n(.*?)(?=\n##|\n#|$)",
            r"### Installation\s*\n(.*?)(?=\n###|\n##|\n#|$)",
        ]
        
        setup_text = ""
        for pattern in setup_patterns:
            match = re.search(pattern, readme_content, re.IGNORECASE | re.DOTALL)
            if match:
                setup_text = match.group(1).strip()
                break
        
        if setup_text:
            # 清理和格式化
            lines = setup_text.split('\n')[:8]  # 最多8行
            cleaned_lines = []
            
            for line in lines:
                line = line.strip()
                if line and len(line) < 300:
                    # 保留代码块
                    if line.startswith('```') or line.startswith('    ') or line.startswith('\t'):
                        cleaned_lines.append(line)
                    # 保留命令
                    elif line.startswith('$') or line.startswith('npm') or line.startswith('pip') or line.startswith('git'):
                        cleaned_lines.append(f"```bash\n{line}\n```")
                    # 保留普通文本说明
                    elif not line.startswith('![') and not line.startswith('[!'):
                        cleaned_lines.append(line)
            
            return "\n".join(cleaned_lines) if cleaned_lines else ""
        
        return ""
    
    def _generate_tech_stack(self, tech_info: Dict) -> str:
        """生成技术栈信息"""
        languages = tech_info.get("languages", {})
        main_language = tech_info.get("language")
        topics = tech_info.get("topics", [])
        
        stack_items = []
        
        if main_language:
            stack_items.append(main_language)
        
        # 添加其他主要语言
        for lang, percentage in sorted(languages.items(), key=lambda x: x[1], reverse=True)[:3]:
            if lang != main_language:
                stack_items.append(lang)
        
        # 添加技术主题
        tech_topics = [topic for topic in topics if any(keyword in topic.lower() 
                      for keyword in ['react', 'vue', 'angular', 'node', 'express', 'django', 'flask', 'spring'])]
        stack_items.extend(tech_topics[:2])
        
        return " • ".join(stack_items) if stack_items else ""
    
    def _format_date(self, date_str: str) -> str:
        """格式化日期"""
        if not date_str:
            return "未知"
        
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime("%Y-%m-%d")
        except:
            return date_str[:10] if len(date_str) >= 10 else date_str
    
    def _generate_footer(self) -> str:
        """生成报告脚注"""
        footer = f"""## 📝 报告说明

<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
- 🤖 本报告基于 GitHub API 自动生成
- 📅 数据更新时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- 🌟 星标数等统计信息为生成时的实时数据
- 📚 项目信息来源于各项目的 README 文档
- 💡 热度指数计算方式: 星标数 + Fork数 × 0.5
</div>

## 🔗 相关链接

- [GitHub API 文档](https://docs.github.com/en/rest)
- [项目数据获取器源码](https://github.com)

---
*本报告由 GitHub 项目分析工具自动生成*"""
        
        return footer


def main():
    parser = argparse.ArgumentParser(description="GitHub 项目 Markdown 报告生成器")
    parser.add_argument("input_file", help="输入的 JSON 数据文件")
    parser.add_argument("--output", "-o", help="输出的 Markdown 文件")
    parser.add_argument("--title", "-t", default="GitHub 热门项目报告", help="报告标题")
    
    args = parser.parse_args()
    
    # 加载数据
    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"读取数据文件失败: {e}")
        return
    
    # 生成报告
    generator = MarkdownReportGenerator()
    
    output_file = args.output
    if not output_file:
        # 自动生成输出文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"github_report_{timestamp}.md"
    
    generator.generate_report(data, output_file, args.title)


if __name__ == "__main__":
    main()
