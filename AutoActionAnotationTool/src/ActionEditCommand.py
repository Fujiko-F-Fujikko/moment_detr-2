# ActionEditCommand.py (修正版)  
from PyQt6.QtGui import QUndoCommand  
  
class ActionDetailModifyCommand(QUndoCommand):  
    def __init__(self, query_result, old_query_text, new_query_text, main_window, description="Modify Action Details"):  
        super().__init__(description)  
        self.query_result = query_result  
        self.old_query_text = old_query_text  
        self.new_query_text = new_query_text  
        self.main_window = main_window  
          
    def redo(self):  
        self.query_result.query_text = self.new_query_text  
        self._update_ui()  
          
    def undo(self):  
        self.query_result.query_text = self.old_query_text  
        self._update_ui()  
      
    def _update_ui(self):  
        if self.main_window:  
            self.main_window.update_display()  
        
        if hasattr(self.main_window, 'edit_widget_manager'):  
            action_editor = self.main_window.edit_widget_manager.get_action_editor()  
            
            # 現在の選択状態を保存  
            current_interval = action_editor.selected_interval  
            current_index = action_editor.selected_interval_index  
            
            # クエリ結果を再設定  
            self.main_window.edit_widget_manager.set_current_query_results(self.query_result)  
            
            # 選択状態を復元  
            if current_interval:  
                action_editor.set_selected_interval(current_interval, current_index)