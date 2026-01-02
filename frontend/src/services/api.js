export async function enviarAvaliacao(dados) {
  const response = await fetch("http://localhost:8000/avaliacao", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dados),
  });

  if (!response.ok) {
    throw new Error("Erro ao enviar avaliação");
  }

  return response.json();
}
