<template>
  <div class="home">
    <h1>客户信息表</h1>

    <!-- 表格切换按钮 -->
    <!-- <div class="button-container">
        <el-button @click="switchTable('table1')">表格1</el-button>
        <el-button @click="switchTable('table2')">表格2</el-button> -->
    <!-- 在这里添加更多的按钮，每个按钮对应一个表格 -->
    <!-- </div> -->

    <div class="table-container"></div>

    <!-- 搜索框 -->
    <el-row>
      <el-col :span="4" class="search-wrapper" stripe>
        <el-input v-model="input" placeholder="请输入查询内容" size="mini"></el-input>
      </el-col>
    </el-row>
    <!-- 搜索框 -->

    <!-- 表格区域 -->
    <el-table
      :data="tables.slice((currentPage - 1) * pageSize, currentPage * pageSize)"
      stripe
      :cell-style="{ textAlign: 'center' }"
      :header-cell-style="{ textAlign: 'center' }"
    >
      <el-table-column prop="client_id" label="客户编号" width="100" sortable />
      <el-table-column prop="client_name" label="姓名" />
      <el-table-column prop="phone_number" label="手机号码" />
      <el-table-column prop="address" label="地址" />

      <!-- 修改添加记录方框 -->
      <el-table-column label="操作" width="210">
        <template slot="header">
          <div
            style="
              display: flex;
              justify-content: space-between;
              align-items: center;
            "
          >
            <span class="op">操作</span>
            <el-button size="mini" class="add" @click="add" icon="el-icon-plus"
              >添加一条记录</el-button
            >
          </div>
        </template>
        <!-- 修改添加记录方框 -->
        <template slot-scope="scope">
          <el-button
            type="info"
            size="mini"
            @click="handEdit(scope.$index, scope.row)"
            icon="el-icon-edit"
            round
            >编辑</el-button
          >
          <el-popconfirm
            title="确认删除吗？"
            @confirm="handDelete(scope.$index, scope.row)"
          >
            <el-button
              type="danger"
              size="mini"
              icon="el-icon-delete"
              round
              slot="reference"
              >删除</el-button
            >
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>

    <!-- 分页器 -->
    <div class="block" style="margin-top: 15px">
      <el-pagination
        align="center"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[1, 5, 8, 10, 20]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="table.length"
      >
      </el-pagination>
    </div>

    <!-- 弹出窗 -->
    <el-dialog
      :title="title"
      :visible="dialogVisible"
      width="30%"
      :before-close="handleClose"
    >
      <el-form :model="form" ref="form" label-width="70px">
        <el-form-item label="客户编号" prop="client_id">
          <el-input v-model="form.client_id" autocomplete="off" />
        </el-form-item>

        <el-form-item label="姓名" prop="client_name">
          <el-input v-model="form.client_name" autocomplete="off" />
        </el-form-item>

        <el-form-item label="手机号码" prop="phone_number">
          <el-input
            v-model="form.phone_number"
            autocomplete="off"
            :placeholder="'请输入11位手机号码'"
            maxlength="11"
          />
        </el-form-item>

        <el-form-item label="地址" prop="address">
          <el-input v-model="form.address" autocomplete="off" />
        </el-form-item>
        
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="reset">重置</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
  
<script>
export default {
  name: "Home",
  data() {
    return {
      table: [],
      dialogVisible: false,
      title: "",
      form: {
        client_id: "",
        client_name: "",
        phone_number: "",
        address: "",
        //判断是add还是update
        // dirty: 0
      },
      nameRules: [{ required: true, message: "请输入姓名", trigger: "blur" }],
      phoneRules: [
        { required: true, message: "请输入手机号码", trigger: "blur" },
        {
          pattern: /^1[3456789]\d{9}$/,
          message: "请输入正确的手机号码",
          trigger: "blur",
        },
      ],
      addressRules: [
        { required: true, message: "请输入地址", trigger: "blur" },
      ],
      currentPage: 1, // 当前页码
      total: 1000, // 总条数
      pageSize: 8, // 每页的数据条数
      input:'',  //查询输入框内容
    };
  },

  created() {
    this.init();
  },
  methods: {
    init() {
      this.$axios.get("/all_client").then((res) => {
        console.log(res);
        this.table = res.data;
      });
    },
    add() {
      this.dialogVisible = true;
      this.title = "添加记录";
      this.form = { new: "" };
    },
    handEdit(index, row) {
      this.dialogVisible = true;
      this.title = "编辑记录";
      this.form = JSON.parse(JSON.stringify(row));
    },
    handDelete(index, row) {
      // 从行数据中提取出 id
      let id = JSON.parse(JSON.stringify(row)).client_id; // 修改4

      // 发送 DELETE 请求删除指定 id 的数据
      this.$axios.delete(`/delete_client?client_id=${id}`).then((res) => {
        // 根据响应中的 code 判断操作是否成功
        if (res.code == 200) {
          // 如果成功，显示成功的通知，并重新初始化数据
          this.$notify.success({
            title: "成功",
            message: res.msg,
            duration: 2000,
          });
          this.init(); // 重新初始化数据
        } else {
          // 如果失败，显示失败的通知
          this.$notify.error({
            title: "失败",
            message: res.msg,
            duration: 2000,
          });
        }
      });
    },

    handleClose() {
      this.dialogVisible = false;
      this.init();
    },
    reset() {
      let id = undefined;
      if ("client_id" in this.form) {
        id = this.form.client_id;
      }
      this.form = {};
      if (id != undefined) this.form.client_id = id;
    },
    save() {
      this.$refs["form"].validate((valid) => {
        // 判断是否通过验证
        console.log("修改1");
        if (valid) {
          console.log(this.form);
          // client_id原本不存在，现在自己加上去了，所以难以作为判断条件
          if (!("new" in this.form)) {
            // if (this.formc'd.dirty) {
            console.log("修改");

            this.$axios.put("/update_client", this.form).then((res) => {
              if (res.code == 200) {
                let _this = this;
                this.$notify.success({
                  title: "成功",
                  message: res.msg,
                  duration: 2000,
                  onClose: function () {
                    _this.handleClose();
                  },
                });
              } else {
                this.$notify.error({
                  title: "错误",
                  message: res.msg,
                  duration: 2000,
                });
              }
            });
          } else {
            console.log("添加");
            // this.form.dirty = 1;
            this.$axios.post("/add_client", this.form).then((res) => {
              if (res.code == 200) {
                let _this = this;
                this.$notify.success({
                  title: "成功",
                  message: res.msg,
                  duration: 2000,
                  onClose: function () {
                    _this.handleClose();
                  },
                });
              } else {
                this.$notify.error({
                  title: "错误",
                  message: res.msg,
                  duration: 2000,
                });
              }
            });
          }
        }
      });
    },
    //每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.currentPage = 1;
      this.pageSize = val;
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
    },
  },
  computed:{
        tables() { //在你的数据表格中定义tabels
		   const input = this.input
			 if (input) {
				// console.log("input输入的搜索内容：" + this.input)
				return this.table.filter(data => {
					console.log("object:" + Object.keys(data))
					return Object.keys(data).some(key => {
						return String(data[key]).toLowerCase().indexOf(input) > -1
					})
				})
			}
			return this.table
		}
  },
};
</script>
  
<style>
h1 {
  text-align: center;
  margin: 50px 0;
}

.el-table {
  width: 80% !important;
  margin: 0 auto;
}

.el-button {
  margin: 0 5px;
}

span.op {
  display: inline-block;
  margin-left: 6px;
}

.el-dialog__body {
  padding-bottom: 0;
}
</style>
<style>
.button-container {
  display: flex;
  flex-direction: column;
  /* 将按钮垂直排列 */
  margin-bottom: 10px;
  /* 可以根据需要调整按钮之间的间距 */
}
</style>
  