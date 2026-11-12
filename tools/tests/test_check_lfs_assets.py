"""Integrity checks must reject pointers or bytes that do not match the catalog."""
import hashlib
import json

import pytest

from tools.check_lfs_assets import load_assets, verify_file


def test_pointer_and_materialized_bytes_share_exact_identity(tmp_path):
    source=b'%PDF-1.7\nverified publication bytes\n'
    item={'path':'01-papers/T1-test/2025-example-X01/paper.pdf',
          'bytes':len(source),'sha256':hashlib.sha256(source).hexdigest()}
    p=tmp_path/'paper.pdf'
    p.write_bytes(source)
    assert verify_file(p,item,True)=='materialized'
    pointer=('version https://git-lfs.github.com/spec/v1\noid sha256:'+item['sha256']+'\nsize '+str(len(source))+'\n').encode()
    p.write_bytes(pointer)
    assert verify_file(p,item)=='pointer'
    with pytest.raises(ValueError,match='has not been downloaded'):
        verify_file(p,item,True)
    p.write_bytes(pointer.replace(('size '+str(len(source))).encode(),b'size 1'))
    with pytest.raises(ValueError,match='does not match'):
        verify_file(p,item)
    p.write_bytes(source+b'changed')
    with pytest.raises(ValueError,match='do not match'):
        verify_file(p,item)


def test_manifest_cannot_publish_private_paths(tmp_path):
    p=tmp_path/'06-data/reading-assets.json';p.parent.mkdir()
    p.write_text(json.dumps({'files':[{'path':'99-archive/local/private.md',
                                     'bytes':3,'sha256':'a'*64}]}))
    with pytest.raises(ValueError,match='Invalid reading-asset'):
        load_assets(tmp_path)
