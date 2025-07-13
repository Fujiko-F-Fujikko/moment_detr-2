# ResultsDisplayManager.py (修正版)  
from PyQt6.QtWidgets import QListWidget, QListWidgetItem  
from PyQt6.QtCore import QObject, pyqtSignal, Qt  
from typing import Optional  
from ResultsDataController import ResultsDataController  
  
class ResultsDisplayManager(QObject):  
    """結果表示の管理を担当するクラス"""  
      
    # シグナル定義  
    intervalSelected = pyqtSignal(object)  # query_result  
      
    def __init__(self, results_controller: ResultsDataController):  
        super().__init__()  
        self.results_controller = results_controller  
        self.results_list: Optional[QListWidget] = None  
          
        # ResultsDataControllerのシグナル接続を修正  
        self.results_controller.resultsLoaded.connect(self.update_display)  
        self.results_controller.resultsFiltered.connect(self.update_display)  
        self.results_controller.resultsUpdated.connect(self.update_display)  
      
    def set_ui_components(self, results_list: QListWidget):  
        """UI要素を設定"""  
        self.results_list = results_list  
        if self.results_list:  
            self.results_list.itemClicked.connect(self._on_item_clicked)  
              
            # 初期表示を更新（データが既に読み込まれている場合）  
            if self.results_controller.is_results_loaded():  
                self.update_display()  
      
    def update_display(self, results=None):  
        """表示を更新"""  
        if not self.results_list:  
            print("DEBUG: results_list is None")  
            return  
          
        # リストをクリア  
        self.results_list.clear()  
          
        # フィルタされた結果を取得  
        if results is None:  
            filtered_results = self.results_controller.get_filtered_results()  
        else:  
            filtered_results = results  
          
        print(f"DEBUG: Updating display with {len(filtered_results)} results")  
          
        # 各結果をリストに追加  
        for i, result in enumerate(filtered_results):  
            try:  
                interval_count = len(result.relevant_windows) if hasattr(result, 'relevant_windows') else 0  
                item_text = f"{result.query_text} ({interval_count} intervals)"  
                item = QListWidgetItem(item_text)  
                item.setData(Qt.ItemDataRole.UserRole, result)  
                self.results_list.addItem(item)  
                print(f"DEBUG: Added item {i}: {item_text}")  
            except Exception as e:  
                print(f"DEBUG: Error adding item {i}: {e}")  
      
    def _on_item_clicked(self, item: QListWidgetItem):  
        """アイテムクリック時の処理"""  
        query_result = item.data(Qt.ItemDataRole.UserRole)  
        self.intervalSelected.emit(query_result)
      
    def select_result_by_query_text(self, query_text: str):  
        """クエリテキストで結果を選択"""  
        if not self.results_list:  
            return  
          
        for i in range(self.results_list.count()):  
            item = self.results_list.item(i)  
            query_result = item.data(Qt.ItemDataRole.UserRole)  
            if query_result and query_result.query_text == query_text:  
                self.results_list.setCurrentItem(item)  
                break  
      
    def force_refresh(self):  
        """強制的に表示を更新"""  
        print("DEBUG: Force refresh called")  
        self.update_display()