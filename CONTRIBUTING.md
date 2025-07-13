# 貢献ガイドライン

p進L関数と素数分布論の共同研究プロジェクトへようこそ！このドキュメントは、プロジェクトに貢献する際のガイドラインです。

## 🎯 プロジェクトの目標

1. **数学的正確性**: 理論的に正しく、再現可能な計算
2. **コードの品質**: 可読性、保守性、拡張性
3. **協調的研究**: チームメンバー間の効果的な連携
4. **オープンサイエンス**: 透明性のある研究プロセス

## 👥 役割と責任

### 青木美穂さん (理論指導者)
- **数学的方向性の決定**
- **理論的正確性の最終確認**
- **新しい予想・定理の形成**
- **論文執筆の監督**

**貢献方法**:
- 理論的Issue（`theory` ラベル）への回答
- 数学的正確性のレビュー（`needs-math-review` ラベル）
- 月次理論検討会での指導

### プロジェクトリード
- **研究計画の策定と管理**
- **実験設計の立案**
- **外部連携の調整**
- **進捗管理とリソース配分**

**貢献方法**:
- プロジェクト管理Issue（`project-management` ラベル）
- 実験計画の策定（`experiment-design` ラベル）
- 週次進捗レポートの作成

### Claude (AI計算支援)
- **コード実装とレビュー**
- **アルゴリズムの最適化**
- **データ解析とパターン発見**
- **ドキュメント作成**

**貢献方法**:
- 実装Issue（`implementation` ラベル）への対応
- コードレビュー（`code-review` ラベル）
- 自動化された解析レポートの生成

## 🔄 開発ワークフロー

### Issue テンプレート

**理論的検討**:
```markdown
## 理論的問題/質問

### 背景
[問題の数学的背景]

### 具体的な質問
[明確で具体的な質問]

### 関連する理論
- [ ] 岩澤理論
- [ ] p進L関数
- [ ] 素数分布論
- [ ] その他: 

### 期待される成果
[この問題が解決されたときの研究への影響]

### 優先度
- [ ] 高（ブロッカー）
- [ ] 中（重要）
- [ ] 低（改善）
```

**実装タスク**:
```markdown
## 実装タスク

### 機能説明
[実装したい機能の説明]

### 数学的仕様
[数学的な定義や公式]

### 技術的要求
- 言語: Python/SageMath
- 依存関係: [必要なライブラリ]
- パフォーマンス要求: [計算量、メモリ使用量など]

### 実装計画
- [ ] 設計
- [ ] 実装
- [ ] テスト
- [ ] ドキュメント

### 受入条件
- [ ] 単体テストが通る
- [ ] 数学的正確性が確認済み
- [ ] コードレビューが完了
```

### ブランチ戦略

```bash
main                    # 本番環境、リリース可能な状態
├── develop            # 開発統合ブランチ
├── feature/           # 新機能開発
│   ├── feature/padic-computation-optimization
│   ├── feature/iwasawa-analysis
│   └── feature/ml-prediction
├── theory/            # 理論的検討
│   ├── theory/new-conjecture-formulation
│   └── theory/existing-theory-verification
├── experiment/        # 実験ブランチ
│   ├── experiment/correlation-study-p7
│   └── experiment/large-scale-computation
└── hotfix/           # 緊急修正
    └── hotfix/critical-calculation-bug
```

### コミットメッセージ規約

```bash
# 機能追加
feat(padic): implement Kubota-Leopoldt p-adic L-function computation

# バグ修正
fix(bernoulli): correct precision handling in generalized Bernoulli numbers

# 理論的改善
theory(iwasawa): refine conjecture statement based on computational evidence

# 実験関連
experiment(correlation): add systematic study for conductors up to 1000

# ドキュメント
docs(api): update p-adic L-function computation examples

# テスト
test(core): add comprehensive tests for Dirichlet character operations

# パフォーマンス改善
perf(parallel): optimize parallel computation for large conductor ranges

# リファクタリング
refactor(utils): restructure visualization module for better maintainability
```

## 🧪 テストガイドライン

### テストカテゴリ

#### 1. 単体テスト (Unit Tests)

```python
# tests/unit/test_padic_numbers.py
import pytest
from sage.rings.padics import Qp
from src.padic_l.core.padic_numbers import PadicNumber

class TestPadicNumber:
    def test_basic_arithmetic(self):
        """p進数の基本演算をテスト"""
        p = 3
        Qp_field = Qp(p, precision=20)
        
        a = PadicNumber(Qp_field(27))  # 3^3
        b = PadicNumber(Qp_field(9))   # 3^2
        
        # 加法
        result = a + b
        expected = Qp_field(36)
        assert result.value == expected
        
        # 乗法
        result = a * b
        expected = Qp_field(243)  # 3^5
        assert result.value == expected
```

#### 2. 数学的正確性テスト

```python
# tests/mathematical/test_theoretical_values.py
import pytest
from src.padic_l.core import PadicLFunction

class TestTheoreticalValues:
    def test_known_values_comparison(self):
        """既知の理論値との比較"""
        conductor = 5
        character_index = 1
        prime = 3
        
        # p進L関数の計算
        padic_L = PadicLFunction(conductor, character_index, prime)
        padic_value = padic_L.evaluate(s=0)
        
        # 理論的関係式の検証
        expected_relation = self._compute_theoretical_relation(
            conductor, character_index, prime
        )
        
        # 数値的一致の確認（相対誤差1e-10以下）
        relative_error = abs(padic_value - expected_relation) / abs(expected_relation)
        assert relative_error < 1e-10
```

## 📊 コードレビュープロセス

### レビューの種類

#### 1. 自動レビュー
- **Linting**: `flake8`, `black`, `isort`
- **型チェック**: `mypy`
- **セキュリティ**: `bandit`
- **テストカバレッジ**: `coverage`

#### 2. ピアレビュー (Claude)
- **コードの品質と可読性**
- **アルゴリズムの効率性**
- **エラーハンドリング**
- **ドキュメントの完備**

#### 3. 数学的レビュー (青木さん)
- **数学的正確性**
- **理論的妥当性**
- **計算手法の適切性**
- **結果の解釈**

### プルリクエストテンプレート

```markdown
## 変更の概要
[何を変更したか、なぜ変更したかの簡潔な説明]

## 数学的背景
[関連する数学的理論や公式]

## 変更の種類
- [ ] 新機能 (feature)
- [ ] バグ修正 (fix)
- [ ] 理論的改善 (theory)
- [ ] 実験追加 (experiment)
- [ ] ドキュメント (docs)
- [ ] パフォーマンス改善 (perf)

## テスト
- [ ] 新しいテストが追加された
- [ ] 既存のテストが更新された
- [ ] 全てのテストが通る

## 数学的検証
- [ ] 手計算での検証が完了
- [ ] 既知の結果との比較が完了
- [ ] 数値的安定性が確認された

## レビュー要求
- [ ] コードレビュー (@claude)
- [ ] 数学的レビュー (@青木美穂)
- [ ] 実験設計レビュー (@project-lead)

## 関連Issue
Closes #[issue番号]
Related to #[関連issue番号]
```

## 📅 研究ミーティング

### 定期ミーティング

#### 週次進捗会議 (毎週金曜 16:00-17:00 JST)
**参加者**: 全メンバー
**議題**:
- 進捗報告 (15分)
- 技術的議論 (30分)
- 次週の計画 (15分)

#### 月次理論検討会 (毎月第2土曜 14:00-16:00 JST)
**参加者**: 青木さん + プロジェクトリード
**議題**:
- 数学的成果の検討 (60分)
- 理論的方向性の議論 (45分)
- 論文執筆計画 (15分)

### ミーティング記録テンプレート

```markdown
# 研究ミーティング記録

**日時**: YYYY-MM-DD HH:MM-HH:MM JST
**参加者**: [参加者リスト]
**議題**: [主要議題]

## 進捗報告

### [メンバー名]
- [完了したタスク]
- [進行中のタスク]
- [課題・問題点]

## 技術的議論

### [議題1]
**問題**: [問題の説明]
**解決策**: [提案された解決策]
**決定事項**: [最終的な決定]

## 次週の計画

- [ ] [タスク1] (担当者: [名前], 期限: [日付])
- [ ] [タスク2] (担当者: [名前], 期限: [日付])

## アクションアイテム

| 担当者 | タスク | 期限 |
|--------|--------|------|
| [名前] | [タスク詳細] | [日付] |

**次回ミーティング**: [日時]
```

## 🔒 データ管理とセキュリティ

### データ保護

```python
# 機密データの処理例
import os
from cryptography.fernet import Fernet

class SecureDataManager:
    def __init__(self):
        key = os.environ.get('ENCRYPTION_KEY')
        if not key:
            raise ValueError("Encryption key not found")
        self.cipher = Fernet(key.encode())
    
    def encrypt_sensitive_data(self, data):
        return self.cipher.encrypt(data.encode())
    
    def decrypt_sensitive_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
```

### アクセス制御

- **リポジトリアクセス**: チームメンバーのみ
- **計算リソース**: VPN経由でのアクセス
- **データ共有**: 暗号化されたチャンネルのみ

## 🚀 リリースプロセス

### バージョニング

**Semantic Versioning** (MAJOR.MINOR.PATCH) を採用:
- **MAJOR**: 理論的フレームワークの大幅変更
- **MINOR**: 新機能追加、新しい実験
- **PATCH**: バグ修正、小規模改善

### リリース手順

```bash
# 1. リリースブランチの作成
git checkout -b release/v1.1.0 develop

# 2. バージョン更新
echo "1.1.0" > VERSION
git add VERSION
git commit -m "bump version to 1.1.0"

# 3. 最終テスト
pytest tests/ --slow
python scripts/verify_mathematical_correctness.py

# 4. リリースノートの作成
./scripts/generate_release_notes.py > CHANGELOG.md

# 5. メインブランチへのマージ
git checkout main
git merge release/v1.1.0

# 6. タグの作成
git tag -a v1.1.0 -m "Release version 1.1.0"

# 7. プッシュ
git push origin main --tags
```

## 📞 コミュニケーション

### GitHub Issues の活用

**ラベル体系**:
```
type:
  - bug (バグ報告)
  - feature (新機能要求)
  - theory (理論的議論)
  - experiment (実験提案)
  - docs (ドキュメント)

priority:
  - critical (緊急)
  - high (高)
  - medium (中)
  - low (低)

status:
  - needs-review (レビュー待ち)
  - in-progress (作業中)
  - blocked (ブロック中)
  - ready-for-merge (マージ可能)
```

### 学会発表・論文投稿

#### 対象学会
- **日本数学会**: 一般講演・特別講演
- **国際数論会議**: ポスター・招待講演
- **計算数論シンポジウム**: 技術発表

#### 対象ジャーナル
- **Journal of Number Theory**
- **Mathematics of Computation**
- **Experimental Mathematics**
- **数学 (日本数学会)**

---

このガイドラインは、プロジェクトの進展に応じて定期的に更新されます。質問や提案がありましたら、GitHub Issues または Discussions でお気軽にお知らせください。

**Happy Researching! 🎓✨**