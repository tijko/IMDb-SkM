#!/usr/bin/env python

import wx
import requests


class SkM_UI(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(530, 250))

        vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(14)

        self.Centre()

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        st = wx.StaticText(panel, label='Movie Title')
        st.SetFont(font)

        hbox.Add(st, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(parent=panel)
        hbox.Add(self.tc, proportion=1)
        vbox.Add(hbox, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        self.genre = wx.CheckBox(panel, -1, pos=(5, 180), label='Genre')
        self.rated = wx.CheckBox(panel, -1, pos=(135, 180), label='Rated')
        self.lang = wx.CheckBox(panel, -1, pos=(265, 180), label='Languages')
        self.poster = wx.CheckBox(panel, -1, pos=(395, 180), label='IMDb Poster')

        self.url = wx.CheckBox(panel, -1, pos=(5, 90), label='IMDb URL')
        self.ID = wx.CheckBox(panel, -1, pos=(135, 90), label='IMDb ID')
        self.cntry = wx.CheckBox(panel, -1, pos=(265, 90), label='Country')
        self.location = wx.CheckBox(panel, -1, pos=(395, 90), label='Filming Location')

        self.writer = wx.CheckBox(panel, -1, pos=(5, 120), label='Writers')
        self.plot = wx.CheckBox(panel, -1, pos=(135, 120), label='Plot Synopsis')
        self.year = wx.CheckBox(panel, -1, pos=(265, 120), label='Year')
        self.runtme = wx.CheckBox(panel, -1, pos=(395, 120), label='Runtime')

        self.release = wx.CheckBox(panel, -1, pos=(5, 150), label='Release')
        self.director = wx.CheckBox(panel, -1, pos=(135, 150), label='Directors')
        self.actor = wx.CheckBox(panel, -1, pos=(265, 150), label='Actors')
        self.rating = wx.CheckBox(panel, -1, pos=(395, 150), label='Rating')

        self.select_all = wx.CheckBox(panel, -1, pos=(25, 220), label='Select All')

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.OkBtn = wx.Button(parent=panel, label='Ok', size=(70, 30))
        self.ClsBtn = wx.Button(parent=panel, label='Close', size=(70, 30))
        hbox2.Add(self.OkBtn, flag=wx.RIGHT, border=15)
        hbox2.Add(self.ClsBtn, flag=wx.RIGHT, border=15)

        self.Bind(wx.EVT_BUTTON, self.results, self.OkBtn)
        self.Bind(wx.EVT_BUTTON, self.stpexit, self.ClsBtn)
        self.Bind(wx.EVT_CHECKBOX, self.chkall, self.select_all)

        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT|wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
        self.Show()

    def stpexit(self, event):
        self.Destroy()

    def chkall(self, event):
        self.genre.SetValue(event.IsChecked())
        self.rated.SetValue(event.IsChecked())
        self.lang.SetValue(event.IsChecked())
        self.poster.SetValue(event.IsChecked())

        self.url.SetValue(event.IsChecked())
        self.ID.SetValue(event.IsChecked())
        self.cntry.SetValue(event.IsChecked())
        self.location.SetValue(event.IsChecked())

        self.writer.SetValue(event.IsChecked())
        self.plot.SetValue(event.IsChecked())
        self.year.SetValue(event.IsChecked())
        self.runtme.SetValue(event.IsChecked())

        self.release.SetValue(event.IsChecked())
        self.director.SetValue(event.IsChecked())
        self.actor.SetValue(event.IsChecked())
        self.rating.SetValue(event.IsChecked())

    def results(self, event):
        m = ''
        data = self.tc.GetValue()
        data = [str(i) for i in data.split(' ')]
        req = requests.get('http://www.imdbapi.org/?title=%s' % data)
        try:
            data = req.json()[0]
            m = m + '\n------------------------------------------------------------------------'
            m = m + '\n'
            m = 'Search Results For : %s' % data['title']
            m = m + '\n'
            m = m + '\n************************************************************************'
            m = m + '\n'

            if self.director.GetValue():
                d = ''
                for director in data['directors']:
                    d = d + director + ', '
                d = d.rstrip(', ')
                m = m + '\n'
                m = m + '\nDirectors: %s' % d

            if self.writer.GetValue():
                w = ''
                for writer in data['writers']:
                    w = w + writer + ', '
                w = w.rstrip(', ')
                m = m + '\n'
                m = m + '\nWriters: %s' % w

            if self.actor.GetValue():
                a = ''
                for actor in data['actors']:
                    a = a + actor + ', '
                a = a.rstrip(', ')
                m = m + '\n'
                m = '\nActors/Actresses: %s' % a

            if self.rating.GetValue():
                m = m + '\n'
                m = m + '\nMovie Rating: %s' % data['rating']

            if self.rated.GetValue():
                m = m + '\n'
                m = m + '\nRated: %s' % data['rated']

            if self.lang.GetValue():
                l = ''
                for lang in data['language']:
                    l = l + lang + ', '
                l = l.rstrip(', ')
                m = m + '\n'
                m = m + '\nLanguage: %s' % l

            if self.poster.GetValue():
                m = m + '\n'
                m = m + '\nPoster Url: %s' % data['poster']

            if self.url.GetValue():
                m = m + '\n'
                m = m + '\nIMDB address: %s' % data['imdb_url']

            if self.ID.GetValue():
                m = m + '\n'
                m = m + '\nIMDB id: %s' % data['imdb_id']

            if self.plot.GetValue():
                m = m + '\n'
                m = m + '\nPlot: %s' % data['plot_simple']

            if self.release.GetValue():
                rel = str(data['release_date'])
                m = m + '\n'
                m = m + '\nRelease Date: %s' % rel[4:6] + ' ' + rel[6:8] + ' ' + rel[:4]

            if self.year.GetValue():
                m = m + '\n'
                m = m + '\nYear: %s' % data['year']

            if self.location.GetValue():
                m = m + '\n'
                m = m + '\nFilming Locations: %s' % data['filming_locations']

            if self.runtme.GetValue():
                r = ''
                for runtime in data['runtime']:
                    r = r + runtime + ', '
                r = r.rstrip(', ')
                m = m + '\n'
                m = m + '\nTotal Runtime: %s' % r

            if self.cntry.GetValue():
                c = ''
                for cntry in data['country']:
                    c = c + cntry + ', '
                c = c.rstrip(', ')
                m = m + '\n'
                m = m + '\nCountry: %s' % c

            if self.genre.GetValue():
                g = ''
                for genre in data['genres']:
                    g = g + genre + ', '
                g = g.rstrip(', ')
                m = m + '\n'
                m = m + '\nGenre: %s' % g
            m = m + '\n________________________________________________________________________'

            dialog = wx.MessageDialog(self, m, style=wx.OK)
            dialog.ShowModal()
            dialog.Destroy()
        except KeyError:
            dialog = wx.MessageDialog(self, 'Make sure you have the correct title!', style=wx.OK)
            dialog.ShowModal()
            dialog.Destroy()
        return

if __name__ == '__main__':
    app = wx.App(False)
    frame = SkM_UI(None, 'IMDb Shortcut')
    app.MainLoop()

