import { Stagehand } from "@browserbasehq/stagehand";
import fs from "fs";
import dotenv from "dotenv";
dotenv.config();

async function main() {
  const stagehand = new Stagehand({
    env: "LOCAL",
    modelName: "gpt-4o-mini",
    modelClientOptions: { apiKey: process.env.OPENAI_API_KEY },
  });
  await stagehand.init();

  await stagehand.page.goto("https://doubleu.twa.rentmanager.com/Shared/Home");

  const operator = stagehand.agent();

  const user = "dsonmezalpan@gmail.com";
  const pass = "Biltrocks123!";
  const prompt = `
    1) Log in with username "${user}" and password "${pass}".
    2) After login, find the account balance. You're looking for things like Balance Due, Balance, Account Balance, Current Balance, etc. and a single amount.
    3) Extract just the numeric balance value.
  `.trim();

  console.log("Agent is acting…");
  const { actions } = await operator.execute(prompt);

  const filtered = actions.filter(a => a.type !== "screenshot");
  fs.writeFileSync("session.json", JSON.stringify(filtered, null, 2));
  console.log(`✅ Saved session.json (${filtered.length} actionable steps)`);

  await stagehand.close();
}

main().catch(console.error);
