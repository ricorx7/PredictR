# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainwindow.py'],
             pathex=['C:\\Users\\rico\\Documents\\rti_code\\python\\PredictR\\venv\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\rico\\Documents\\rti_code\\python\\PredictR', 'C:\\Users\\rico\\Documents\\rti_code\\python\\PredictR\PredictR_view' ,'C:\\Users\\rico\\Documents\\rti_code\\python\\PredictR\\rti_python'],
             binaries=[],
             datas=[('rti_python\\ADCP\\Predictor\\predictor.json', 'rti_python\\ADCP\\Predictor\\.'), ('rti.ico', '.'), ('rti_python\\ADCP\\AdcpCommands.json', 'rti_python\\ADCP\\.')],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PredictR',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='rti.ico')
