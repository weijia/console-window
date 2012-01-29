#!/usr/local/env python

import pygtk
pygtk.require('2.0')
import gtk

def motion_cb(wid, context, x, y, time):
    l.set_text('\n'.join([str(t) for t in context.targets]))
    context.drag_status(gtk.gdk.ACTION_COPY, time)
    # Returning True which means "I accept this data".
    return True

def drop_cb(wid, context, x, y, time):
    # Some data was dropped, get the data
    wid.drag_get_data(context, context.targets[-1], time)
    return True

def got_data_cb(wid, context, x, y, data, info, time):
    # Got data.
    print data.data
    print data.format
    print data.selection
    print data.target
    l.set_text(data.get_text())
    context.finish(True, False, time)

w = gtk.Window()
w.set_size_request(200, 150)
w.drag_dest_set(0, [], 0)
w.connect('drag_motion', motion_cb)
w.connect('drag_drop', drop_cb)
w.connect('drag_data_received', got_data_cb)
w.connect('destroy', lambda w: gtk.main_quit())
l = gtk.Label()
w.add(l)
w.show_all()

gtk.main()
