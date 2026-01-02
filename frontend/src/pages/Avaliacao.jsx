{resultado && (
  <div
    style={{
      marginTop: "20px",
      padding: "15px",
      borderRadius: "8px",
      backgroundColor:
        resultado.resultado.cor === "verde"
          ? "#d4edda"
          : resultado.resultado.cor === "amarelo"
          ? "#fff3cd"
          : "#f8d7da",
      color: "#000",
    }}
  >
    <h2>Resultado da Avaliação</h2>

    <p><strong>Nível de Risco:</strong> {resultado.resultado.nivel}</p>
    <p>{resultado.resultado.descricao}</p>
  </div>
)}
