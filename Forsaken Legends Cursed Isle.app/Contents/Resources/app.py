import json
import os
import webview

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data.json')
INDEX_FILE = os.path.join(BASE_DIR, 'index.html')

class Api:
    def _read_data(self):
        if not os.path.exists(DATA_FILE):
            return {}
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {}
        except Exception:
            return {}

    def _write_data(self, data):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def save_slot(self, slot, name, value):
        data = self._read_data()
        if 'Version' not in data:
            data['Version'] = {'value': '2.18.62'}
        data[f'slot{slot}'] = {
            'name': name,
            'value': value
        }
        self._write_data(data)
        return True

    def get_all_saves(self):
        data = self._read_data()
        if 'Version' not in data:
            data['Version'] = {'value': 'Unknown'}
            self._write_data(data)
        return data

if __name__ == '__main__':
    api = Api()
    webview.create_window(
        'Forsaken Legends Cursed Isle',
        INDEX_FILE,
        js_api=api,
        width=1100,
        height=900,
        min_size=(960, 720),
        resizable=True
    )
    webview.start(http_server=True)
