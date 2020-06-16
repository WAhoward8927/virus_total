# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['entrance.py'],
             pathex=['.\\all_func.py', '.\\catch_file.py', '.\\general_func.py', '.\\grep_dict.py', '.\\storge_result.py', '.\\globals.py', 'D:\\wang\\py_workdir\\VT_application(proxy29)'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='virustotal_ncsist',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
