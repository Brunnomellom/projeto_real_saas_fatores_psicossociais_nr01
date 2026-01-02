import { useState } from "react";

function AvaliacaoForm() {
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);

  const enviarAvaliacao = async () => {
    setLoading(true);

    const payload = {
      mpf: [5, 6, 7, 4, 6],
      demanda: [4, 4, 3, 4],
      controle: [2, 2, 3, 2],
      apoio: [3, 3, 4, 3],
      severidade: 3
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/avaliacao", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      setResultado(data);
    } catch (error) {
      alert("Erro ao enviar avaliação");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Formulário Psicossocial</h2>

      <button onClick={enviarAvaliacao} disabled={loading}>
        {loading ? "Enviando..." : "Enviar Avaliação"}
      </button>

      {resultado && (
        <pre style={{ marginTop: "20px", background: "#eee", padding: "10px" }}>
          {JSON.stringify(resultado, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default function AvaliacaoForm() {
  return <h2>COMPONENTE OK ✅</h2>;
}


