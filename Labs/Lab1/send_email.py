from gmail import GMail, Message
from random import choice

gmail=GMail('titeoteoti321@gmail.com','126hoangquocviet')
template="Chào sếp, hôm nay em nghỉ nhé, em bị {{sick}}. Em thấy {{symptom}}"
sickness_list=["thương hàn","kiết lị","tiêu chảy"]
sickness=choice(sickness_list)
symptom="đau bụng"
content=template.replace("{{sick}}", sickness).replace("{{symptom}}",symptom)
message=Message('Xin nghi lam',to='nguyenhonglam9396@gmail.com',text=content)
gmail.send(message)


