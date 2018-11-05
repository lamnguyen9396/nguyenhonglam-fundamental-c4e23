from gmail import GMail, Message
from random import choice

gmail=GMail('titeoteoti321@gmail.com','126hoangquocviet')
template='''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay em ngủ dậy thấy đau bụng, b&aacute;c sĩ bảo em bị Ebola.</p>
<p>Sếp cho em nghỉ nh&eacute;.</p>
<p>Nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-smile.gif" alt="smile" /></p>
'''
# sickness_list=["thương hàn","kiết lị","tiêu chảy"]
# sickness=choice(sickness_list)
# symptom="đau bụng"
# content=template.replace("{{sick}}", sickness).replace("{{symptom}}",symptom)
message=Message('Xin nghi lam',to='nguyenhonglam9396@gmail.com',html=template)
from datetime import datetime
time=datetime.now().strftime('%H:%M')
while time>'7:30':
    gmail.send(message)


