# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/peyto/VSCodeProjects/SpeedReader/src/cli.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/peyto/VSCodeProjects/SpeedReader/Lib/site-packages/customtkinter', 'customtkinter/'), ('C:/Users/peyto/VSCodeProjects/SpeedReader/src/main.py', '.')],
    hiddenimports=['customtkinter', 'urllib3', 'beautifulsoup4', 'nltk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SpeedReader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SpeedReader',
)
