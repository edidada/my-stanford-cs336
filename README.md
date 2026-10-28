# Stanford CS336 自学工作区

基线：Stanford **Spring 2026 — Language Modeling from Scratch**，2026-10-28 核对。

- [官方课程、课表和视频入口](https://cs336.stanford.edu/)
- [学习路线](docs/learning-roadmap.md)：面向 10 年以上软件开发经验，按每周 10–12 小时规划。
- `upstream/assignment1-basics` 至 `assignment5-alignment`：官方学生起始代码及各自作业 PDF。
- `upstream/lectures`：配套讲义代码。
- [提交锁定清单](docs/upstream-lock.json)：完整 SHA；Git 索引中的 gitlink 是实际版本基准。

选择当前课程直接链接的 5 个实验和讲义；未引入排行榜、2024/2025 历史仓库或第三方答案。课程使用 Python/PyTorch/uv，沿用上游工具链。

版本细节：当前课程链接的 A1 README 标题仍写 Spring 2025，保留官方原样，并以 SHA 明确版本；A2/A4 自带 staff 的基础模型代码，属于官方提供的实验依赖。建议完成 A1 后再阅读这些实现。

## 获取与校验

```bash
git clone --recurse-submodules git@github.com:edidada/my-stanford-cs336.git
cd my-stanford-cs336
git submodule update --init --recursive
python scripts/verify_upstream.py
```

不要运行 `git submodule update --remote` 来复现本基线。submodule 锁定的是父仓库记录的提交，而不是上游 main 的未来状态。更新时显式 fetch、checkout 指定 SHA，同时更新锁定清单并审查差异。

开始 A1：进入 `upstream/assignment1-basics`，阅读 README、作业 PDF 和 `pyproject.toml`，然后按上游说明使用 `uv sync` 与 `uv run pytest`。起始代码含待实现内容，测试失败不代表获取失败。

## 学习代码的保存

`upstream/` 保持官方基线。实际作答可复制到独立 Git 仓库或自己的 fork；若直接修改 submodule，应先创建学习分支，并把提交推送到自己的 fork，再让父仓库引用可公开获取的提交。只提交父仓库不会保存 submodule 内未提交的修改。

本仓库 Actions 只验证 URL、gitlink 与锁定 SHA 一致，不执行尚未完成的作业或 GPU 训练。训练产物和数据放在被忽略的根目录中；各 submodule 有独立的忽略规则。
