import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Loading from "./Loading.jsx";

const BlogPost = () => {
  const [blog, setBlog] = useState(null);
  const { blogID } = useParams(); // Move useParams outside of useEffect

  useEffect(() => {
    fetch(`/api/getPost/${blogID}`)
      .catch((err) => {
        throw err;
      })
      .then((data) => data.json())
      .then((data) => setBlog(data));
  }, [blogID]);

  return blog ? (
    <div className="prose mx-auto ">
      <div className="flex flex-col">
        <h1>{blog.title}</h1> <h2>{blog.username}</h2>
      </div>
      <div className="flex"> {blog.content} </div>
    </div>
  ) : (
    <Loading />
  );
};

export default BlogPost;
