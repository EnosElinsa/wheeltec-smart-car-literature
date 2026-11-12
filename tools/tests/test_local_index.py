"""Generator regressions that run without a browser or local PDFs."""
import json,re
from tools.local_index import render,venue_family
from tools.corpus import Entry


def test_venue_families_preserve_journals_and_group_conference_editions():
    assert venue_family('2026 IEEE International Conference on Robotics and Automation (ICRA)') == 'ICRA'
    assert venue_family('2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)') == 'IROS'
    assert venue_family('Proceedings of The 9th Conference on Robot Learning') == 'CoRL'
    assert venue_family('Robotics: Science and Systems XXI') == 'RSS'
    assert venue_family('The International Journal of Robotics Research') == venue_family('International Journal of Robotics Research')
    assert venue_family('IEEE Transactions on Robotics') == 'IEEE Transactions on Robotics'
    assert venue_family('') == 'Unspecified venue'


def test_render_preserves_metadata_without_script_injection():
    title = '</script><script>window.injected=true</script>'
    entry = Entry({'code':'TEST1','title':title,'venue':'IEEE Transactions on Robotics','publication_type':'journal','theme':'T1','bibliographic_year':'2026','citation_status':'derived','view_group':'main'},'T1-perception-localization',None,False)
    page=render([entry])
    payload=re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>',page,re.S).group(1)
    rows=json.loads(payload)
    assert rows[0]['title']==title
    assert '<script>' not in payload
    assert rows[0]['publication_type']=='journal'
    assert rows[0]['citation_status']=='derived'
    assert render([entry])==page


def test_reading_interface_does_not_count_administrative_identities():
    entries = [Entry({'code':group,'title':group,'view_group':group},
                     'T1-perception-localization',None,False)
               for group in ('main','surveys','excluded','pending')]
    page = render(entries)
    payload = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>',page,re.S).group(1)
    rows = json.loads(payload)
    assert {r['code'] for r in rows} == {'main','surveys'}
    assert all(r['venue_family'] == '' for r in rows)
