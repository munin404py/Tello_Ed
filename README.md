# Tello_Ed: Telloドローンプログラミング学習リポジトリ

ようこそ！ このリポジトリは、DJIのトイドローン「Tello」を使って、プログラミングの基礎から応用（Web API、コンピュータビジョン、SLAMの概念）までを体系的に学ぶための教材です。

`munin404py/slam-ad` という高度なプロジェクトを理解することを最終目標に、一歩ずつステップアップしていきましょう。

## 🎯 この教材のゴール

*   Pythonを使ってTelloドローンを制御できるようになる。
*   FastAPIを使って簡単なWeb APIを構築できるようになる。
*   OpenCVを使ってカメラ映像を取得し、簡単な画像処理ができるようになる。
*   フロントエンドとバックエンドが連携するWebアプリケーションの仕組みを理解する。
*   SLAMのような高度な技術を学ぶための基礎知識を身につける。

## 📚 学習の進め方

この教材は、`lessons` ディレクトリの中にステップ・バイ・ステップ形式で格納されています。

### 🌟 初心者の方へ

**Pythonを触るのが初めて、または2〜3時間程度しか経験がない方は、以下の順番で進めてください：**

1.  **Step 00**: 環境構築 - Pythonとエディタのインストール
2.  **Step 0**: Python基礎 - f文字列、クラス、継承などの基本概念
3.  **Step 1以降**: Telloドローンのプログラミング

### 📝 学習のコツ

各ステップのディレクトリには、そのステップの目標と詳しい解説が書かれた `README.md` と、動作するサンプルコードが含まれています。

1.  まず、各ステップの `README.md` をよく読み、その回の目標を理解します。
2.  次に、サンプルコードを自分の手で打ち込んで（写経して）動かしてみます。
3.  コードが動いたら、中の数字を変えたり、処理の順番を入れ替えたりして「**もしこう変えたら、どうなるか？**」という実験をたくさんしてみてください。エラーを出すことは、最高の学びです。

---

### 📖 レッスン一覧

#### 🔰 準備編（Python初心者向け）

*   [**Step 00: プログラミング環境の準備** (`lessons/step-00-environment-setup`)](./lessons/step-00-environment-setup)
    *   **目標:** Python、エディタをインストールし、ポートやネットワークの基本を理解する。
    *   **対象:** プログラミング完全初心者

*   [**Step 0: Pythonの基本** (`lessons/step-0-python-basics`)](./lessons/step-0-python-basics)
    *   **目標:** 変数、f文字列、関数、クラス、継承など、Pythonの基礎を学ぶ。
    *   **対象:** Pythonを2〜3時間しか触ったことがない方

#### 🚁 ドローンプログラミング編

*   [**Step 1: こんにちは、Tello！** (`lessons/step-01-hello-tello`)](./lessons/step-01-hello-tello)
    *   **目標:** Telloドローンに初めて接続し、バッテリー残量を取得してみる。

*   [**Step 2: 基本的な飛行制御** (`lessons/step-02-basic-movement`)](./lessons/step-02-basic-movement)
    *   **目標:** ドローンを離陸させ、少し動かして、着陸させる。

*   [**Step 3: Web APIでドローンを操る** (`lessons/step-03-web-api`)](./lessons/step-03-web-api)
    *   **目標:** FastAPIを使ってWeb APIを作り、ブラウザからドローンを操作する。

*   [**Step 4: Telloの目を見る（映像取得）** (`lessons/step-04-camera-stream`)](./lessons/step-04-camera-stream)
    *   **目標:** OpenCVを使い、Telloのカメラ映像をPCの画面に表示する。

*   [**Step 5: 操作パネルを作る（フロントエンド）** (`lessons/step-05-simple-frontend`)](./lessons/step-05-simple-frontend)
    *   **目標:** 簡単なHTMLとJavaScriptで、ブラウザにドローン操作用のボタンを作る。

*   [**Step 6: 簡単な物体追跡** (`lessons/step-06-object-tracking`)](./lessons/step-06-object-tracking)
    *   **目標:** OpenCVの画像処理で、特定の色を見つけてその座標を取得する。

*   [**Step 7: SLAMへの道** (`lessons/step-07-intro-to-slam`)](./lessons/step-07-intro-to-slam)
    *   **目標:** `slam-ad`プロジェクトの核心であるSLAMが、どのような技術なのかを概念的に理解する。

---

## 必要なもの

### ハードウェア
*   DJI Tello ドローン

### ソフトウェア
*   Python 3.7以降（インストール方法は [Step 00](./lessons/step-00-environment-setup) を参照）
*   テキストエディタ (Visual Studio Code推奨、セットアップは [Step 00](./lessons/step-00-environment-setup) を参照)

### その他
*   インターネット接続環境

### 📌 学習の前提知識

*   **Python初心者の方**: [Step 00](./lessons/step-00-environment-setup) と [Step 0](./lessons/step-0-python-basics) から始めてください
*   **Pythonに慣れている方**: Step 1 から始められます

それでは、さっそく始めてみましょう！