import type { Actions } from "./$types";

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const name = formData.get("name") as string;
    const description = formData.get("description") as string;

    const item = { name, description };
    console.log(item);

    try {
      const response = await fetch("http://localhost:8000/items/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(item),
      });

      if (!response.ok) {
        throw new Error("Failed to submit form");
      }

      const result = await response.json();
      return { success: true, data: result };
    } catch (error) {
      console.error("Error:", error);
      return { success: false, error: "Failed to submit form" };
    }
  },
};
