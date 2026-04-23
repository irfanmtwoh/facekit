from connection.db_officekit import get_db
from model.database import get_database

class AllEmp:
    def __init__(self, company_code):
        self.company_code = company_code
        self.conn = get_db(company_code)
        self.db = get_database(company_code)
        self.encoding_db = self.db[f"encodings_{company_code}"]
        
    def get_all_emp(self, offset=0, limit=10, search=None, branch_id=None):
        where_conditions = []
        where_params = []
        
        if search:
            where_conditions.append("(Emp_Code LIKE %s OR First_Name LIKE %s)")
            search_param = f"%{search}%"
            where_params.extend([search_param, search_param])
            
        if branch_id:
            where_conditions.append("BranchID = %s")
            where_params.append(branch_id)
            
        where_clause = ""
        if where_conditions:
            where_clause = "WHERE " + " AND ".join(where_conditions)
        
        count_q = f"SELECT COUNT(*) as total FROM HR_EMP_MASTER {where_clause}"
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(count_q, tuple(where_params))
        total_count = cursor.fetchone()['total']
        
        data_q = f"""
            SELECT First_Name, Last_Name, Emp_Code, Gender, BranchID FROM HR_EMP_MASTER
            {where_clause}
            ORDER BY Emp_Code
            OFFSET %s ROWS FETCH NEXT %s ROWS ONLY
        """
        data_params = where_params + [int(offset), int(limit)]
        cursor.execute(data_q, tuple(data_params))
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            if row.get('Emp_Code'):
                row['Emp_Code'] = str(row['Emp_Code']).strip()

        emp_codes = [row['Emp_Code'] for row in rows]
        existing_codes = set()
        if emp_codes:
            existing_docs = self.encoding_db.find(
                {"employee_code": {"$in": emp_codes}},
                {"employee_code": 1}
            )
            existing_codes = {doc['employee_code'] for doc in existing_docs}

        data = []
        for row in rows:
            data.append({
                **row,
                "exist": row['Emp_Code'] in existing_codes
            })

        return {
            "data": data, 
            "total": total_count, 
            "offset": int(offset), 
            "limit": int(limit)
        }

    
