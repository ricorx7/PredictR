# -*- mode: python -*-
# USED FOR DEBUGGING

block_cipher = None


a = Analysis(['mainwindow.py'],
             pathex=['G:\\RTI\\python\\PredictR', 'C:\\Users\\rico\\AppData\\Roaming\\Python\\Python35\\site-packages\\PyQt5\\Qt\\bin', 'G:\\rti\\python\\PredictR\\rti_python'],
             binaries=[],
             datas=[('rti_python/ADCP/Predictor/predictor.json', 'rti_python/ADCP/Predictor/.'), ('rti.ico', '.'), ('rti_python/ADCP/AdcpCommands.json', 'rti_python/ADCP/.')],
             hiddenimports=[],
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
          exclude_binaries=True,
          name='PredictR_OneDir',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='rti.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PredictR_OneDir')
