from locust import HttpUser, task


class TortoiseUser(HttpUser):
    @task
    def get_and_update_and_get(self) -> None:
        create_meeting_response = self.client.post(
            url="/v1/mysql/meetings",
        )

        # 응답 상태 코드 확인
        if create_meeting_response.status_code == 200:
            try:
                url_code = create_meeting_response.json()["url_code"]
            except ValueError as e:
                print(f"JSON 파싱 오류: {e}")
                print("응답 내용:", create_meeting_response.text)
                return  # 오류가 발생하면 이후 작업을 중지
        else:
            print(f"Error: {create_meeting_response.status_code}")
            return

        self.client.patch(
            url=f"/v1/mysql/meetings/{url_code}/date_range",
            json={
                "start_date": "2025-01-01",
                "end_date": "2025-02-20",
            },
            name="patch_date_range_mysql",
        )

        self.client.post(
            url="/v1/mysql/participants",
            json={
                "name": "test_name",
                "meeting_url_code": url_code,
            },
            name="post_participants_mysql",
        )

        self.client.get(
            url=f"/v1/mysql/meetings/{url_code}",
            name="get_meetings_mysql",
        )