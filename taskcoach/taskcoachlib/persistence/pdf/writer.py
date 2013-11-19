'''
Task Coach - Your friendly task manager
Copyright (C) 2004-2013 Task Coach developers <developers@taskcoach.org>

Task Coach is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Task Coach is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re, generator, os
from taskcoachlib.domain import date
from xhtml2pdf import pisa


class PDFWriter(object):

#Export to PDF
#author: Erik Ivarsson 

    def __init__(self, fd, filename):
        self.__fd = fd
        self.__filename = filename
        self.__maxDateTime = date.DateTime()
        
    def write(self, viewer, settings, selectionOnly, columns = None):
        
        
        textToPdf, count = generator.viewer2pdf(viewer, settings, selectionOnly, columns)
        print textToPdf
        self.__fd.close()
        resultFile = open(self.__filename, "w+b")
        pisa.CreatePDF(textToPdf, resultFile)
        resultFile.close()
        
        return count

    @classmethod
    def contextsAndProjects(cls, task):
        subjects = []
        for category in task.categories():
            subject = category.subject(recursive=True).strip()
            if subject and subject[0] in ('@', '+'):
                subject = re.sub(r' -> ', '->', subject)
                subject = re.sub(r'\s+', '_', subject)
                subjects.append(subject)
        return ' ' + ' '.join(sorted(subjects)) if subjects else ''
    