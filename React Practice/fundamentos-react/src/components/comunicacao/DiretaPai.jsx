import React from "react";
import DiretaFilho from "./DiretaFilho";

const DiretaPai = (props) => {
  return (
    <div>
      <DiretaFilho name="Brandon" age={32} nerd={true}></DiretaFilho>
      <DiretaFilho name="Ryan" age={33} nerd={false}></DiretaFilho>
    </div>
  );
};

export default DiretaPai;
