'''
Automatically send email, to multiple sources.
The email are djusted to the source by aplying multiple text replaces
'''

import smtplib
import getpass
from dataclasses import dataclass, field


@dataclass
class AutoEmails:
    '''
    Automatically send email, to multiple sources.
    The email are djusted to the source by aplying multiple text replaces
    '''
    email: str
    text: str
    _server: object = field(init=False)

    def _initialize_server(self, port=465):
        ''' connect and login to gmail '''

        password = getpass.getpass(prompt='Password:')
        self._server = smtplib.SMTP_SSL('smtp.gmail.com', port)
        self._server.login(self.email, password)

    def send_emails(self, client_emails: str | list, **kwargs):
        ''' execute n times the function that sends an email '''
        if isinstance(client_emails, str):
            self._send_email(client_emails, **kwargs)
        else:
            for client_email in client_emails:
                self._send_email(client_email, **kwargs)

    def _send_email(self, client_email: str, **kwargs):
        '''
        Replace some part of the text to be adjusted to the client.
        Send the emails
        '''
        text_copy = self.text
        for key, value in kwargs:
            text_copy.replace(key, value)
        self._server.sendmail(self.email, client_email, text_copy)

    def _close_server(self):
        ''' close gmail '''
        self._server.close()

