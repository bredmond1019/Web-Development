import React from "react";
import produtos from "../../data/produtos";
import "./TabelaProdutos.css";

const TabelaProdutos = (props) => {
  const produtosTR = produtos.map((produto, i) => {
    return (
      <tr key={produto.id} className={i % 2 == 0 ? "Even" : ""}>
        <td>{produto.id}</td>
        <td>{produto.name}</td>
        <td>${produto.price}</td>
      </tr>
    );
  });

  return (
    <div className="TabelaProdutos">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name of Product</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>{produtosTR}</tbody>
      </table>
    </div>
  );
};

export default TabelaProdutos;
