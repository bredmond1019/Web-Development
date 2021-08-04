import "./App.css";
import { useState, useEffect } from "react";
import ArticleList from "./components/ArticleList";
import Form from "./components/Form";
import APIService from "./components/APIService";

function App() {
  const [articles, setArticles] = useState([]);
  const [editedArticle, setEditedArticle] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/get", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setArticles(resp))
      .catch((error) => console.log(error));
  }, []);

  const editArticle = (article) => {
    setEditedArticle(article);
  };

  const deleteArticle = (article) => {
    APIService.DeleteArticle(article.id)
      .then((resp) => console.log(resp))
      .catch((error) => console.log(error));
  };

  const updatedData = (article) => {
    console.log("I'm in updatedData APP: ", article);
    const new_article = articles.map((my_article) => {
      if (my_article.id === article.id) {
        return article;
      } else {
        return my_article;
      }
    });
    setArticles(new_article);
  };

  const openForm = () => {
    setEditedArticle({ title: "", body: "" });
  };

  const insertedArticle = (article) => {
    const new_articles = [...articles, article];
    setArticles(new_articles);
  };

  return (
    <div className="App">
      <div className="row">
        <div className="col">
          <h1 className="title">Flask and React Project</h1>
        </div>
        <div className="col">
          <button className="btn btn-success" onClick={openForm}>
            Insert Article
          </button>
        </div>
      </div>

      <ArticleList
        articles={articles}
        editArticle={editArticle}
        deleteArticle={deleteArticle}
      />
      {editedArticle ? (
        <Form
          article={editedArticle}
          updatedData={updatedData}
          insertedArticle={insertedArticle}
        />
      ) : null}
    </div>
  );
}

export default App;
