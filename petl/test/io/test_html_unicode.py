# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
# N.B., do not import unicode_literals in tests


import codecs
from tempfile import NamedTemporaryFile
from petl.test.helpers import eq_


from petl.io.html import touhtml


def test_touhtml():

    # exercise function
    tbl = ((u'name', u'id'),
           (u'Արամ Խաչատրյան', 1),
           (u'Johann Strauß', 2),
           (u'Вагиф Сәмәдоғлу', 3),
           (u'章子怡', 4))
    fn = NamedTemporaryFile().name
    touhtml(tbl, fn, lineterminator='\n')

    # check what it did
    f = codecs.open(fn, mode='r', encoding='utf-8')
    actual = f.read()
    expect = u"""<table class='petl'>
<thead>
<tr>
<th>name</th>
<th>id</th>
</tr>
</thead>
<tbody>
<tr>
<td>Արամ Խաչատրյան</td>
<td style='text-align: right'>1</td>
</tr>
<tr>
<td>Johann Strauß</td>
<td style='text-align: right'>2</td>
</tr>
<tr>
<td>Вагиф Сәмәдоғлу</td>
<td style='text-align: right'>3</td>
</tr>
<tr>
<td>章子怡</td>
<td style='text-align: right'>4</td>
</tr>
</tbody>
</table>
"""
    eq_(expect, actual)
