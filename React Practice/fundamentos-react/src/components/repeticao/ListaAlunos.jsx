import React from "react";
import alunos from "../../data/alunos";

const ListaAlunos = (props) => {
  const alunosLI = alunos.map((aluno) => {
    return (
      <li key={aluno.id}>
        {aluno.id}) {aluno.name} -> {aluno.grade}
      </li>
    );
  });

  return (
    <div>
      <ul style={{ listStyle: "none" }}>{alunosLI}</ul>
    </div>
  );
};

export default ListaAlunos;
