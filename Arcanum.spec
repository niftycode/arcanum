# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Arcanum',
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
    icon=['assets/app-icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Arcanum',
)
app = BUNDLE(
    coll,
    name='Arcanum.app',
    icon='assets/app-icon.icns',
    bundle_identifier='de.nicefield.Arcanum',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'Arcanum',
                'CFBundleTypeIconFile': 'app-icon.icns',
                'LSItemContentTypes': ['de.nicefield.Arcanum'],
                'LSHandlerRank': 'Owner'
            }
        ],
        'CFBundleIdentifier': 'de.nicefield.Arcanum',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleGetInfoString': 'Bodo Schönfeld © 2025'
    },
)
