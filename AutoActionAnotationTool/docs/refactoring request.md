# refactoring request

AutoActionAnnotationToolのリファクタリングをしています。 古い実装の設計書はdocs/old_class_diaglam.md, ソースコードはAutoActionAnnotationTool/oldフォルダ以下にあります。新しい実装の計画書はdocs/refactor_class_diaglam.md, ソースコードはAutoActionAnnotationTool/srcフォルダ以下にあります。 現状リファクタリングの実装は完了していますが、元の実装に比べて機能が足りてないところやバグがあります。
今わかっているのは以下です。
- [x] 1. DetectionResultsに表示される要素をクリックすると、各クエリの2番目以降の要素を選択してもTimeline上やActionEditタブ上では1番目の要素が選択されてしまう。
- [x] 2. StepEditタブで、AddStepボタンで新規追加したり、Steps一覧ででいずれかの要素を選択してプロパティを変更した後に、編集していた要素への選択状態が外れてしまう。
- [ ] 3. Timeline上でドラッグして新規Interval追加する機能がなくなっている（Step/Edit 両方）
- [ ] 4. Timeline上でドラッグしてIntervalの位置を変更する機能がおかしい（Step/Edit 両方）
- [ ] 5. Timeline上でマウスボタンを押した後、ドラッグ操作できるときにマウスカーソルが変わらない（元の使用では矢印カーソルになったり手カーソルになったりするはず）
- [x] 6. Action/Step両方のEditタブ上で、テキストボックスに入力して確定しても変更が反映されない
- [x] 7. Action/Step両方のEditタブ上で、Delete Intervalボタンが効かない
- [x] 8. Actionタブ上で、Add Intervalボタンが効かない
- [x] 9. Stepタブ上で、start/endの時間の変更が効かない。入力⇒Enter設楽元の数字に戻る

古い実装を正として、これらの点に関して古い実装の通りに動作するように修正してください。