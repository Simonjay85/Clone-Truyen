// Hàm làm sạch dữ liệu chống SQL Injection và XSS
function vanhiep_sanitize_js(input) {
    // Đảm bảo input là một chuỗi
    if (typeof input !== 'string') {
        input = String(input);
    }

    // Loại bỏ các ký tự nguy hiểm để tránh XSS
    input = input.replace(/<script[^>]*?>.*?<\/script>/gi, '');
    input = input.replace(/<\/?\w(?:[^"'>]|"[^"]*"|'[^']*')*>/gmi, '');

    // Chuyển các ký tự đặc biệt thành mã HTML
    input = input.replace(/&/g, '&amp;');
    input = input.replace(/</g, '&lt;');
    input = input.replace(/>/g, '&gt;');
    input = input.replace(/"/g, '&quot;');
    input = input.replace(/'/g, '&#x27;');
    input = input.replace(/\//g, '&#x2F;');

    // Loại bỏ các ký tự SQL Injection phổ biến
    input = input.replace(/--/g, '');
    input = input.replace(/;/g, '');
    input = input.replace(/\\/g, '');
    input = input.replace(/\b(SELECT|UPDATE|DELETE|INSERT|DROP|UNION|TRUNCATE|ALTER|CREATE|REPLACE|RENAME|GRANT|REVOKE|REPAIR|OPTIMIZE|ANALYZE|SHOW|DESCRIBE|EXPLAIN)\b/gi, '');

    return input;
}
