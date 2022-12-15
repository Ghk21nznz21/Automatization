import smtplib 
import getpass 
from dataclasses import dataclass, field

@dataclass 
class AutoEmails:
    email: str 
    text: str 
    _server: object = field(init=False)
    
    def _initialize_server(self, port=465):
        password = getpass.getpass(prompt='Password:')
        self._server = smtplib.SMTP_SSL('smtp.gmail.com', port)
        self._server.login(self.email, password)

    def send_emails(self, client_emails: str | list, **kwargs):
        if isinstance(client_emails, str):
            self._send_email(client_emails, **kwargs)
        else:
            for client_email in client_emails:
                self._send_email(client_email, **kwargs)

    def _send_email(self, client_email: str, **kwargs):
        ''' 
        Replace key by value -> kwargs 
        '''
        text_copy = self.text.copy()        
        for key, value in kwargs:
            text_copy.replace(key, value)
        self._server.sendmail(self.email, client_email, text_copy)
    
    def _close_server(self):
        self._server.close()



