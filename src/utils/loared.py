import json

from fastapi import UploadFile


class ReaderJSONFile:

    async def load(self, file: UploadFile) -> dict:
        data = json.loads(
            await file.read()
        )

        return data
                    