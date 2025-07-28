# README

## 環境構築

### python

3.11.2

### コマンド手順

```cmd
python -m venv venv
source venv/Scripts/activate

python -m pip install --upgrade pip
pip install numpy==1.26.4
pip install torch==2.1.2+cu118 torchvision==0.16.2+cu118 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

## 実行手順

1. スクリプトによるアクション検出実行
```cmd
cd run_inference
./run_inference.sh <video_path> <query1> [query2] [query3] ... 

./run_inference.sh ../stt/20250724_object-annotation/H1125062070282_2025-06-20_12-39-19_0.mp4 "LeftHand_Hold_Camera Rear Cabin_None_None" "RightHand_Pickup_Cotton Swab_None_None" "BothHands_Hold_Camera Rear Cabin_None_None" "RightHand_Putdown_Camera Rear Cabin_Clear Tray_None"

```
* ※ queryは`<LeftHand | RightHand | BothHands | Other>_<Verb>_<Maniqulated Object Name>_<Target Object Name>_<Tool Name>`の形式を想定していますが、どんな形式・文でも指定できます。ただし英語のみ。
* 手順2のツールでアノテーション結果を編集したい場合は、この形式に従って指定してください。指定するものがない場合は`None`と指定してください。

2. GUIツールでアノテーション結果の確認&編集

```cmd
cd ../ # ルートディレクトリに戻る
python AutoActionAnotationTool/src/MainApplicationWindow.py --video <path_to_video> --results <path_to_json_generated_by_step_1> 
```