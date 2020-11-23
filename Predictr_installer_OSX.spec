# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainwindow.py'],
             pathex=['/Users/rico/Documents/rti/python/PredictR/rti_python', '/Users/rico/Documents/rti/python/PredictR/venv/lib/python3.7/site-packages/PyQt5/Qt/bin', '/Users/rico/Documents/rti/python/PredictR', '/Users/rico/Documents/rti/python/PredictR/PredictR_view'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainwindow',
          debug=True,
          strip=False,
          upx=True,
          console=True )
app = BUNDLE(exe,
             name='PredictR.app',
             icon='rti.ico',
             bundle_identifier=None)
