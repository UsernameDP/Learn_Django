import React, { useEffect, useState } from "react";
import BlogCard from "./BlogCard.jsx";

const BlogList = () => {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    //TODO : set blogs properly else by fetching

    fetch("/api/getAllPosts")
      .then((data) => data.json())
      .then((data) => setBlogs(data));
  }, []);

  return (
    <div
      role="grid"
      className="flex flex-col gap-5 px-20"
    >
      {blogs.map((blog, index) => {
        return (
          <BlogCard
            key={blog.id}
            id={blog.id}
            title={blog.title}
            username={blog.username}
            content={blog.content}
            date={blog.date}
          />
        );
      })}
    </div>
  );
};

export default BlogList;
