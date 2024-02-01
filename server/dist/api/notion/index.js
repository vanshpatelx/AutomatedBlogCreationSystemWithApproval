"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.api_call = void 0;
const { Client } = require("@notionhq/client");
function api_call() {
    return __awaiter(this, void 0, void 0, function* () {
        const notion = new Client({ auth: process.env.NOTION_KEY });
        console.log(process.env.NOTION_KEY);
        (() => __awaiter(this, void 0, void 0, function* () {
            const response = yield notion.pages.create({
                cover: {
                    type: "external",
                    external: {
                        url: "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg",
                    },
                },
                icon: {
                    type: "emoji",
                    emoji: "🥬",
                },
                parent: {
                    type: "page_id",
                    page_id: "e774c7e1-7d70-47ee-99be-6497fbb5ac8b",
                },
                properties: {
                    title: [
                        {
                            text: {
                                content: "Tuscan kale",
                            },
                        },
                    ],
                },
                children: [
                    {
                        object: "block",
                        paragraph: {
                            rich_text: [
                                {
                                    text: {
                                        content: `1. **Bold and Italic:**
                  - This text is **bold**.
                  - _This text is italic_.
               
               2. **Headers:**
                  - ## Second-level heading
                  - ### Third-level heading
               
               3. **Links:**
                  - [Visit OpenAI's website](https://www.openai.com/)
               
               `,
                                    },
                                    href: "https://en.wikipedia.org/wiki/Lacinato_kale",
                                },
                            ],
                            color: "default",
                        },
                    },
                ],
            });
            console.log(response);
        }))();
        (() => __awaiter(this, void 0, void 0, function* () {
            const pageId = 'a849e4a2-a53c-41d9-ba6c-f21798e2ea6c';
            const response = yield notion.pages.retrieve({ page_id: pageId });
            console.log("hello");
            console.log(response);
        }))();
    });
}
exports.api_call = api_call;
