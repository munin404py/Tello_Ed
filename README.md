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
`step-01` から順番に進めていくことをお勧めします。

各ステップのディレクトリには、そのステップの目標と詳しい解説が書かれた `README.md` と、動作するサンプルコードが含まれています。

1.  まず、各ステップの `README.md` をよく読み、その回の目標を理解します。
2.  次に、サンプルコードを自分の手で打ち込んで（写経して）動かしてみます。
3.  コードが動いたら、中の数字を変えたり、処理の順番を入れ替えたりして「**もしこう変えたら、どうなるか？**」という実験をたくさんしてみてください。エラーを出すことは、最高の学びです。

---

### 📖 レッスン一覧

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

*   DJI Tello ドローン
*   Python 3.7以降
*   テキストエディタ (Visual Studio Codeなど)
*   インターネット接続環境

それでは、さっそく `Step 1` から始めてみましょう！