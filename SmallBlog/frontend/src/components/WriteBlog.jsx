import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const WriteBlog = () => {
  const [authenticated, setIsAuthenticated] = useState(false);
  const [title, setTitle] = useState(""); // State for the title
  const [content, setContent] = useState(""); // State for the content

  const navigate = useNavigate();

  // Handler for changes to the title input
  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  // Handler for changes to the content input
  const handleContentChange = (event) => {
    setContent(event.target.value);
  };

  const handleSubmit = (event) => {
    fetch("/api/addPost", {
      method: "POST",
      body: JSON.stringify({ title: title, content: content })
    })
      .then((response) => {
        if (!response.ok) throw new Error("Failed to post");

        return response;
      })
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        navigate("/");
      });
  };
  useEffect(() => {
    fetch("/api/authenticate")
      .then((response) => {
        if (!response.ok) {
          navigate("/");
          return;
        }
        return response;
      })
      .catch((err) => {
        console.error("Failed to authenticate : ", err);
        console.log("helloo?");
        navigate("/");
        return;
      })
      .then((data) => data.json())
      .then((data) => {
        setIsAuthenticated(true);
      });
  }, []);

  return authenticated ? (
    <div className="prose mx-auto flex flex-col gap-5">
      <input
        type="text"
        value={title}
        onChange={handleTitleChange}
        className="  border-2"
        placeholder="Enter title here"
      />

      <textarea
        className="border-2"
        placeholder="Enter content here"
        rows={25}
        value={content}
        onChange={handleContentChange}
      ></textarea>

      <button
        className="w-full bg-blue-500 text-white rounded-sm"
        onClick={handleSubmit}
      >
        Submit
      </button>
    </div>
  ) : (
    <></>
  );
};

export default WriteBlog;
