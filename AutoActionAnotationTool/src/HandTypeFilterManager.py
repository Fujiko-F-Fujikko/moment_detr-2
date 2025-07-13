# HandTypeFilterManager.py (UI管理機能を追加)  
from PyQt6.QtCore import QObject, pyqtSignal  
from typing import List, Dict  
from Results import QueryResults  
from STTDataStructures import QueryParser, QueryValidationError  
  
class HandTypeFilterManager(QObject):  
    """Hand Typeフィルタリングの統合管理クラス"""  
      
    # シグナル定義  
    filterChanged = pyqtSignal(str)  
    resultsGrouped = pyqtSignal(dict)  
      
    def __init__(self):  
        super().__init__()  
        self.current_filter = "All"  
        self.all_results: List[QueryResults] = []  
        self.grouped_results: Dict[str, List[QueryResults]] = {}  
      
    def set_results(self, results: List[QueryResults]):  
        """結果を設定"""  
        self.all_results = results  
        self._update_grouped_results()  
      
    def set_filter(self, hand_type: str):  
        """フィルタを設定"""  
        if self.current_filter != hand_type:  
            self.current_filter = hand_type  
            self.filterChanged.emit(hand_type)  
      
    def get_filtered_results(self) -> List[QueryResults]:  
        """フィルタされた結果を取得"""  
        if self.current_filter == "All":  
            return self.all_results  
          
        return self.grouped_results.get(self.current_filter, [])  
      
    def get_grouped_results(self) -> Dict[str, List[QueryResults]]:  
        """グループ化された結果を取得"""  
        return self.grouped_results  
      
    def _update_grouped_results(self):  
        """結果をHand Type別にグループ化"""  
        self.grouped_results = {  
            'LeftHand': [],  
            'RightHand': [],  
            'BothHands': [],  
            'None': [],  
            'Other': []  
        }  
          
        for result in self.all_results:  
            # Stepクエリの場合は特別処理  
            if result.query_text.startswith("Step:"):  
                self.grouped_results['Other'].append(result)  
                continue  
              
            try:  
                detected_hand_type, _ = QueryParser.validate_and_parse_query(result.query_text)  
                if detected_hand_type in self.grouped_results:  
                    self.grouped_results[detected_hand_type].append(result)  
                else:  
                    self.grouped_results['Other'].append(result)  
            except QueryValidationError:  
                self.grouped_results['Other'].append(result)  
          
        self.resultsGrouped.emit(self.grouped_results)