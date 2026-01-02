fetch("http://localhost:8000/avaliacao", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(dados)
})
.then(res => res.json())
.then(data => console.log(data))
