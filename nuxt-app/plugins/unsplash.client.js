import { createApi } from "unsplash-js";

var unsplash = new createApi({
  accessKey: "U7rXXGFREuyCVwTgAutWXWxetHZ9-kAnYaORSZN_DvU",
});

export default defineNuxtPlugin(() => {
  return {
    provide: {
      unsplash,
    },
  };
});
