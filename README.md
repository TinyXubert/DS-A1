# DS-A1: Data provenance and measurement audit

`A1.ipynb` 审计 UCI Bank Marketing 的 `bank-additional-full.csv`。问题是：这张表的全部输入字段，是否都能在最后一次营销电话之前获得？本作业不训练模型。

报告分为七部分，含十个代码格。正文用英文，执行提示用中文。

## 运行

在 VS Code 打开 `A1.ipynb`，选择内核：

```text
/data2/xuhongbo/DS_HW/DS-A1/.venv/bin/python
```

内核的工作目录应为 `/data2/xuhongbo/DS_HW/DS-A1`。代码使用 `BASE = Path.cwd()`，第一格会检查目录。通常 VS Code 默认使用 Notebook 所在目录；如果启动在父目录，可先在一个临时代码格中执行 `%cd /data2/xuhongbo/DS_HW/DS-A1`，然后删除这个临时格。

按下表从 01 到 10 使用 Shift+Enter 执行，不跳格。重新完整执行前重启内核，避免旧变量影响结果。

| 报告部分 | 代码格 | 你要读懂的证据 |
|---|---|---|
| 1. Question and scope | 01 | 环境、种子、结果目录；条件概率与样本比例的区别 |
| 2. Provenance and DGP | 02、03 | 冻结哈希、来源、许可、电话发生前后的信息边界 |
| 3. Schema | 04 | 表结构、字段类型、允许类别、完整数据字典 |
| 4. Missingness | 05 | NaN 与 unknown 的差异；999 不是经过的天数 |
| 5. Range, duplicate, anomaly | 06、07 | 合理范围、联系历史编码冲突、重复与异常为何不直接删除 |
| 6. Leakage and counterexamples | 08 | duration 的时序问题；关联不能代替可用性证据 |
| 7. Findings and reflection | 09、10 | 数值结果、Data Card、AI 日志、个人核验和摘要 |

每次运行 01 只建立一个 `results/<UTC时间>/` 目录，避免覆盖旧结果。里面保存表格、图、环境、源文件哈希以及报告文件快照。
如遇错误，先保存含报错的 Notebook 副本并保留本次结果目录，再修复、重启内核，从头运行。不要丢弃失败或与预期不符的证据。

## 你需要完成的文字

- 在 Notebook 标题填写姓名。
- 阅读和维护 `DATA_CARD.md`。它是独立报告文件，不再由代码生成。
- 阅读 `DATA_DICTIONARY.csv`，字段含义依据 `data/raw/bank-additional-names.txt`。
- 亲自核对来源并独立复核至少一个数值，在 `AI_USE_LOG.md` 的学生部分写下方法、结果、日期和反思。助手查过来源不等于你完成了核验。
- 审阅 `SUBMISSION_SUMMARY.md` 的英文摘要，并填写稳定 GitHub URL 和 commit/tag。

修改这些 Markdown 文件后，重新执行代码格 10 并保存 Notebook，PDF 才会显示更新后的内容。报告文件与实际数据有变化时，摘要中的数值也需要重新核对。

## 导出包含代码和执行结果的 PDF

先保存已执行的 Notebook（Ctrl+S），再运行：

```bash
cd /data2/xuhongbo/DS_HW/DS-A1
.venv/bin/python export_report.py
```

导出脚本读取已保存的代码和输出，不重新执行。它会拒绝未执行完、带错误或执行次序异常的文件，生成 `A1.html`。

把 HTML 下载到本地，用浏览器打开，按 Ctrl+P，选择“保存为 PDF”，保存为 `A1.pdf`。建议 A4，关闭浏览器自动页眉页脚。检查代码换行、图和长表是否完整，再将 PDF 放回仓库。这个方法不依赖服务器的 LaTeX 或浏览器。

## 环境与磁盘

`.venv` 位于 `/data2`，复用 base 已有依赖，新增包安装在该虚拟环境中。`requirements.txt` 固定直接依赖；每次运行的 `requirements-lock.txt` 记录完整环境，可能含机器相关路径。

新机器可在自己的空虚拟环境中安装：

```bash
python -m pip install -r requirements.txt
```

Notebook 第一格把后续临时文件和 Matplotlib 缓存放在项目目录。若内核启动之前就因根分区满而失败，需要在启动进程的终端预先设置路径：

```bash
cd /data2/xuhongbo/DS_HW/DS-A1
mkdir -p .runtime/tmp .runtime/jupyter .runtime/ipython .runtime/matplotlib
export TMPDIR="$PWD/.runtime/tmp"
export JUPYTER_RUNTIME_DIR="$PWD/.runtime/jupyter"
export JUPYTER_CONFIG_DIR="$PWD/.runtime/jupyter"
export IPYTHONDIR="$PWD/.runtime/ipython"
export MPLCONFIGDIR="$PWD/.runtime/matplotlib"
```

已运行的远程 IDE 未必继承新变量，必要时重新连接。

## 文件和提交

提交需包含已执行的 Notebook、PDF、原始数据与来源/hash、raw results、Data Card、字典及 AI/个人核验记录；平台另需 150 至 300 词结果摘要、稳定仓库 URL 与 commit/tag。

原始数据位于 `data/raw/`。精简前的 Notebook、README、导出脚本和初始生成器保存在 `archive/before_simplification_*/`；旧结果目录保持原样。不要运行存档中的旧生成器。此前未完成的运行也是历史证据，不代表当前稿已通过验证。

`.venv/`、`.runtime/`、`.validation/` 不提交。本次编辑不会自动 push、创建远程仓库或提交课程平台。

## 来源与许可

Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing*. UCI Machine Learning Repository.
https://doi.org/10.24432/C5K306

数据许可：CC BY 4.0。数据页：https://archive.ics.uci.edu/dataset/222/bank+marketing

确切下载时间与 SHA-256：`data/raw/manifest.json`。派生审计结果是本项目新增内容，原始 CSV 保持不变。仓库原有 LICENSE 不替代数据集的许可。
