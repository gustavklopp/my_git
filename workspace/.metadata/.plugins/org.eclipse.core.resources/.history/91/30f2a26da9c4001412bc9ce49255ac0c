from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.rst import RstDocument
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import ObjectProperty, StringProperty
from kivy.event import EventDispatcher
from kivy.lang import Builder
from sqlalchemy import *
# from os.path import join

# db = create_engine('sqlite:///drug_test.db', echo=False)
db = create_engine('sqlite:///rcp_database.db', echo=False)
metadata = MetaData(db)
drugs = Table('rcp_table', metadata, autoload=True)


class SearchDrugScreen(Screen):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    spec_search = ObjectProperty()
    dci_search = ObjectProperty()
            
    def search_drug(self):
        if self.dci_search.active:
            s = drugs.select(drugs.c["Nom en DCI"].startswith(self.search_input.text))
        else:
            s = drugs.select(drugs.c.spec_name.startswith(self.search_input.text))
#         print(s)
        rs = s.execute()
        drug_results = [drug.spec_name for drug in rs]
        self.search_results.item_strings = drug_results
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(drug_results)
        self.search_results._trigger_reset_populate()
  

class DrugButton(ListItemButton):
    pass


class ShowRCPScreen(Screen):
    showrcp_chosen_label = ObjectProperty()
    def update_text(self, chosen_drug):
        self.showrcp_chosen_label.text = chosen_drug

         
class ShowRCPDetailScreen(Screen):
    showrcpdetail_chosen_label = ObjectProperty()
    rcpdetail_grid = ObjectProperty()
    
    def update_text(self, chosen_drug):
        self.showrcpdetail_chosen_label.text = chosen_drug
        self.rcpdetail_grid.clear_widgets()
        
    def display_item(self, chosen_item):
        chosen_drug = self.showrcpdetail_chosen_label.text
#         print("chosen drug inside display_item :", chosen_drug)
        self.rcpdetail_grid.clear_widgets()
        self.rcpdetail_grid.display_grid(chosen_drug, chosen_item)
        
          
class RcpDetail_GridLayout(GridLayout):
    rcpdetail_grid = ObjectProperty()
     
    def display_grid(self, chosen_drug, chosen_item):
#         print("chosen drug :", chosen_drug, "chosen item : ", chosen_item)
        s = drugs.select(drugs.c.spec_name==chosen_drug)
        rs = s.execute()
        drg = rs.fetchone()
 
        '''create the buttons'''
        btn = Button(text=chosen_item, height="30dp", size_hint_y=None)
        lbl = RstDocument(text=str(drg[chosen_item]))
        self.cols = 1
        self.add_widget(btn)
        self.add_widget(lbl)


class Drug_RCPApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(SearchDrugScreen(name='searchdrug'))
        sm.add_widget(ShowRCPScreen(name='showrcp'))
        sm.add_widget(ShowRCPDetailScreen(name='showrcpdetail'))  
        return sm

if __name__ == "__main__":
    Drug_RCPApp().run()