from flask import Flask, render_template, request, jsonify
app=Flask(__name__)

@app.get("/")
def admin(): return render_template("index.html")
@app.get("/ux")
def ux(): return render_template("ux.html")
@app.get("/logica")
def logica(): return render_template("logica.html")
@app.get("/dados")
def dados(): return render_template("dados.html")
@app.get("/testes")
def testes(): return render_template("testes.html")

@app.post("/api/ux/check")
def ux_check():
    d=request.get_json()
    checks=[
      ("Contraste",d.get("contrast")=="alto","O painel industrial precisa ser legível rapidamente."),
      ("Ação crítica",d.get("button")=="forte","A ação principal deve se destacar."),
      ("Navegação",d.get("menu")=="lateral","Em painéis de operação, navegação lateral mantém funções visíveis."),
      ("Texto",d.get("font")=="grande","Informações operacionais precisam de boa leitura."),
      ("Status",d.get("status")=="cores","Estados de máquina ficam mais rápidos de identificar por cor."),
      ("Alertas",d.get("alerts")=="prioridade","Alertas críticos devem aparecer antes dos avisos comuns.")
    ]
    score=round(sum(x[1] for x in checks)/len(checks)*100)
    return jsonify(score=score,approved=score>=80,
      items=[{"name":n,"ok":ok,"tip":tip} for n,ok,tip in checks])

@app.post("/api/logica/check")
def logic_check():
    seq=request.get_json().get("sequence",[])
    correct=["inicio","cracha","turno","epi","decisao","resultado"]
    return jsonify(correct=seq==correct)

@app.post("/api/dados/check")
def data_check():
    a=request.get_json().get("answers",{})
    exp={
      "Ana Souza":"funcionarios","Carlos Lima":"funcionarios","João Alves":"funcionarios",
      "Prensa P-01":"maquinas","Robô R-07":"maquinas","Esteira E-03":"maquinas",
      "Manutenção":"setores","Produção":"setores","Qualidade":"setores",
      "Capacete":"epis","Óculos":"epis","Protetor auricular":"epis"
    }
    c=sum(a.get(k)==v for k,v in exp.items())
    return jsonify(correct=c,total=len(exp),score=round(c/len(exp)*100),approved=c==len(exp))

@app.post("/api/testes/check")
def qa_check():
    found=set(request.get_json().get("found",[]))
    bugs={"matricula","senha","maquina","botao"}
    c=len(found & bugs)
    return jsonify(correct=c,total=4,score=c*25,approved=c==4)

if __name__=="__main__":
    app.run(debug=True)
