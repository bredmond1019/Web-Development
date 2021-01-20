import React from "react";

const PassoForm = (props) => {
  return (
    <div>
      <label htmlFor="">Pass</label>
      <input
        id="passoInput"
        type="number"
        value={props.pass}
        onChange={(e) => props.setPass(+e.target.value)}
      />
    </div>
  );
};

export default PassoForm;
