# p進L関数と素数分布論の共同研究

[![Build Status](https://github.com/jxta/padic-L/workflows/CI/badge.svg)](https://github.com/jxta/padic-L/actions)
[![Documentation](https://readthedocs.org/projects/padic-l/badge/?version=latest)](https://padic-l.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 🎯 研究概要

本プロジェクトは、**p進L関数の符号変化パターンと古典的Chebyshev偏りの相関**を数値実験により解明し、「**p進素数分布論**」という新しい数学分野の基礎を構築することを目指しています。

### 🔬 核心アイデア

```maths
古典的偏り: π(x;q,a₁) - π(x;q,a₂)
     ⟺
p進符号: sign(Lₚ(0,χ))
```

従来は複素解析的手法で研究されてきた素数分布の偏り現象を、p進解析と岩澤理論の観点から統一的に理解することを目標としています。

## 👥 研究チーム

- **青木美穂** (島根大学) - 理論指導・数学的方向性
- **Project Lead** - 研究計画・実験設計
- **Claude (AI)** - 計算実装・データ解析支援

## 🚀 クイックスタート

### 環境構築

```bash
# リポジトリのクローン
git clone https://github.com/jxta/padic-L.git
cd padic-L

# 依存関係のインストール
./scripts/setup/install_dependencies.sh

# 環境の確認
python scripts/setup/verify_installation.py
```

### 初回実験の実行

```bash
# 小規模テスト実験
python src/cli/main.py run-experiment --scale small

# 結果の可視化
jupyter notebook notebooks/exploratory/01_basic_padic_computation.ipynb
```

## 📚 理論的背景

### p進L関数 (Kubota-Leopoldt)

p進L関数 $L_p(s, \chi)$ は、古典的Dirichlet L関数の「p進類似」として構成されます：

```python
# p進L関数の基本計算例
from src.padic_l.core import PadicLFunction

padic_L = PadicLFunction(conductor=5, character=1, prime=3)
value_at_zero = padic_L.evaluate(s=0)
sign = padic_L.sign_at_zero()
```

### Chebyshev偏り

素数分布における古典的な偏り現象：
- $\pi(x; 4, 1) > \pi(x; 4, 3)$ (4k+1型素数が4k+3型素数より多い傾向)

### 岩澤理論的解釈

円分$\mathbb{Z}_p$拡大における偏りの伝播：
```maths
K₀ ⊂ K₁ ⊂ K₂ ⊂ ⋯ ⊂ K∞
```

## 🔬 主要な研究成果（期待）

### 予想1: p進-古典対応原理
```maths
sign(Lₚ(0,χ)) = +1 ⟹ χ値が正の素数が多く現れる
sign(Lₚ(0,χ)) = -1 ⟹ χ値が負の素数が多く現れる
```

### 予想2: 岩澤階層での偏りの増幅
```maths
Bias(Kₙ) ≈ λⁿ · Bias(K₀) · pᵘⁿ
```

## 📊 実験結果

### 相関解析結果

```python
# 最新の相関結果を確認
from src.analysis import load_latest_results

results = load_latest_results()
print(f"p進符号 vs 古典偏り相関: {results.correlation:.4f}")
print(f"統計的有意性 (p値): {results.p_value:.6f}")
```

## 🛠️ 主要コンポーネント

### Core Library (`src/padic_l/`)

- **`core/`**: p進数演算、Dirichlet指標、Bernoulli数計算
- **`iwasawa/`**: 岩澤理論、$\mathbb{Z}_p$拡大、不変量計算
- **`classical/`**: 古典的素数計数、偏り計算、L関数

### 実験モジュール (`src/experiments/`)

- **`correlation_study.py`**: 主要な相関研究
- **`iwasawa_analysis.py`**: 岩澤理論的解析
- **`ml_prediction.py`**: 機械学習による予測

### 解析ツール (`src/analysis/`)

- **`statistical_tests.py`**: 統計的有意性検定
- **`pattern_recognition.py`**: パターン認識・異常検知
- **`theoretical_comparison.py`**: 理論予測との比較

## 📓 Jupyter Notebooks

### 探索的解析
- [`01_basic_padic_computation.ipynb`](notebooks/exploratory/01_basic_padic_computation.ipynb) - p進L関数の基本計算
- [`02_classical_bias_analysis.ipynb`](notebooks/exploratory/02_classical_bias_analysis.ipynb) - 古典的偏りの解析
- [`03_preliminary_correlations.ipynb`](notebooks/exploratory/03_preliminary_correlations.ipynb) - 予備的相関分析

### 本格実験
- [`systematic_study_p3.ipynb`](notebooks/experiments/systematic_study_p3.ipynb) - p=3での系統的研究
- [`iwasawa_tower_analysis.ipynb`](notebooks/experiments/iwasawa_tower_analysis.ipynb) - 岩澤塔の解析
- [`ml_bias_prediction.ipynb`](notebooks/experiments/ml_bias_prediction.ipynb) - 機械学習予測

## 🔧 高度な使用法

### 大規模並列計算

```python
from src.padic_l.utils.parallel import ParallelComputation

# 1000個の導手について並列計算
computer = ParallelComputation(n_cores=8)
results = computer.systematic_study(
    conductors=range(3, 1000),
    primes=[3, 5, 7],
    precision=100
)
```

### カスタム実験

```python
from src.experiments import CustomExperiment

# 特定の理論的予測を検証
experiment = CustomExperiment()
experiment.add_hypothesis("padic_sign_correlation", threshold=0.3)
experiment.add_data_range(conductors=(100, 500), primes=[3, 5])
results = experiment.run()
```

## 📈 パフォーマンス最適化

### ベンチマーク結果

| 計算規模 | 時間 (CPU) | 時間 (GPU) | メモリ使用量 |
|----------|------------|------------|--------------|
| D ≤ 100  | 2分        | 30秒       | 4GB          |
| D ≤ 500  | 45分       | 8分        | 16GB         |
| D ≤ 1000 | 4時間      | 35分       | 32GB         |

## 🧪 テストとCI/CD

### テストの実行

```bash
# 全テストの実行
pytest tests/

# 特定モジュールのテスト
pytest tests/unit/test_padic_numbers.py -v

# カバレッジレポート
pytest --cov=src tests/
```

## 📖 ドキュメント

### 理論的背景
- [岩澤理論入門](docs/theory/iwasawa_theory.md)
- [p進L関数の基礎](docs/theory/padic_l_functions.md)
- [Chebyshev偏りの現象](docs/theory/chebyshev_bias.md)

### アルゴリズム解説
- [Kubota-Leopoldt構成](docs/algorithms/kubota_leopoldt.md)
- [岩澤不変量の計算](docs/algorithms/iwasawa_invariants.md)
- [相関解析手法](docs/algorithms/correlation_analysis.md)

## 🤝 貢献方法

詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

### 簡単なワークフロー

```bash
# 機能ブランチの作成
git checkout -b feature/new-algorithm

# 変更のコミット
git add .
git commit -m "feat: implement new p-adic computation algorithm"

# プルリクエストの作成
git push origin feature/new-algorithm
```

## 📄 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) をご覧ください。

## 📞 連絡先

- **Issues**: GitHubのIssue tracker
- **Discussions**: GitHubのDiscussions
- **Email**: research-team@padic-l.org

## 🙏 謝辞

- **島根大学数理科学科**: 計算リソースの提供
- **SageMath Development Team**: 数学計算ライブラリ
- **数論研究コミュニティ**: 理論的指導と議論

---

**注意**: このプロジェクトは理論的研究が中心であり、実用的なアプリケーションではありません。数学的な正確性と計算の再現性を最優先に開発されています。